import datetime as dt
from library import EX

START = dt.date(2026, 9, 21)
RACE = dt.date(2026, 12, 6)
FLY_OUT = dt.date(2026, 10, 28)
RETURN = dt.date(2026, 11, 17)

rows = []          # detailed plan rows
daymeta = {}       # date -> (focus, label, location)

def item(d, order, exid, sets="", reps="", rest="", load="", note="", km=0, contacts=0, custom=None):
    name = custom if custom else EX[exid]["name"]
    cat = EX[exid]["cat"] if exid in EX else "Other"
    rows.append(dict(date=d, order=order, exid=exid or "", name=name, cat=cat,
                     sets=sets, reps=reps, rest=rest, load=load, note=note,
                     km=km, contacts=contacts))

def day(d, focus, label, location):
    daymeta[d] = dict(focus=focus, label=label, location=location)

# ---------------------------------------------------------------- shared blocks
DAILY5 = [("M08", "3", "5 breaths", "", "", "Exhale fully; flatten the low back"),
          ("M01", "2", "8/side", "", "", ""),
          ("M02", "2", "45s/side", "", "", "Tuck the tailbone BEFORE leaning"),
          ("C01", "2", "8/side", "", "", ""),
          ("C03", "2", "30s/side", "", "", "")]

def add_daily5(d, start_order, tag="Daily 5 mobility"):
    o = start_order
    for exid, s, r, rest, load, note in DAILY5:
        item(d, o, exid, s, r, rest, load, (tag + ". " + note).strip(". ") if note else tag)
        o += 1
    return o

def add_warmup(d, o, style="general"):
    if style == "run":
        item(d, o, "M20", "1", "5 min", "", "", "Brisk walk or very easy jog to start"); o += 1
        item(d, o, "R12", "1", "5-6 min", "", "", "A-skip, B-skip, high knees, butt kicks, carioca, leg swings"); o += 1
    else:
        item(d, o, "M17", "1", "4 min", "", "", "Quads, glute/TFL, calves, t-spine over the roller"); o += 1
        item(d, o, "M08", "2", "5 breaths", "", "", "Pelvic reset before anything loaded"); o += 1
        item(d, o, "M01", "1", "8/side", "", "", ""); o += 1
        item(d, o, "M11", "1", "10/side", "", "", "Check both ankles"); o += 1
        item(d, o, "M02", "1", "40s/side", "", "", ""); o += 1
        item(d, o, "P03", "2", "20m", "", "", "Wakes up the hips and ground contact"); o += 1
    return o

def add_cooldown(d, o, sciatic=True):
    if sciatic:
        item(d, o, "M14", "2", "10/side", "", "", "Stay SHORT of any tingling"); o += 1
    item(d, o, "M13", "2", "40s/side", "", "", "Gentle"); o += 1
    item(d, o, "M07", "1", "45s", "", "", "Finish decompressed"); o += 1
    return o

# ---------------------------------------------------------------- day builders
def d_plyo_power(d, wk, plyo, power, label):
    day(d, "Plyo / Power", label, "Hyrox gym (AM)")
    o = add_warmup(d, 1)
    for exid, s, r, rest, note, c in plyo:
        item(d, o, exid, s, r, rest, "", note, contacts=c); o += 1
    for exid, s, r, rest, load, note in power:
        item(d, o, exid, s, r, rest, load, note); o += 1
    o = add_cooldown(d, o)
    return o

def d_run_easy(d, minutes, strides, label, extra=None):
    day(d, "Running - Easy", label, "Outdoor / treadmill")
    o = add_warmup(d, 1, "run")
    km = round(minutes / 6.2, 1)
    item(d, o, "R01", "1", f"{minutes} min", "", "6:00-6:30 /km", "Conversational the whole way", km=km); o += 1
    if strides:
        item(d, o, "R07", str(strides), "100m", "walk back", "~90% effort", "Relaxed and fast, not a sprint", km=round(strides*0.1,1)); o += 1
    if extra:
        for exid, s, r, rest, load, note in extra:
            item(d, o, exid, s, r, rest, load, note); o += 1
    o = add_daily5(d, o)
    return o

def d_strength(d, main, label, loc="GoodLife"):
    day(d, "Strength", label, loc)
    o = add_warmup(d, 1)
    for exid, s, r, rest, load, note in main:
        item(d, o, exid, s, r, rest, load, note); o += 1
    o = add_cooldown(d, o, sciatic=False)
    return o

def d_run_quality(d, work, label, cd=10):
    day(d, "Running - Quality", label, "Track / outdoor")
    o = add_warmup(d, 1, "run")
    item(d, o, "R01", "1", "12 min", "", "easy", "Warm-up jog", km=2.0); o += 1
    kmtot = 0
    for exid, s, r, rest, load, note, km in work:
        item(d, o, exid, s, r, rest, load, note, km=km); o += 1
        kmtot += km
    item(d, o, "R11", "1", f"{cd} min", "", "very easy", "Cool-down jog", km=round(cd/6.5,1)); o += 1
    o = add_daily5(d, o)
    return o

def d_mobility(d, label="Mobility + Rest"):
    day(d, "Mobility / Rest", label, "Home")
    o = 1
    item(d, o, "M17", "1", "6 min", "", "", "Full circuit"); o += 1
    item(d, o, "M10", "1", "10", "", "", ""); o += 1
    item(d, o, "M09", "2", "8/side", "", "", ""); o += 1
    item(d, o, "M08", "3", "5 breaths", "", "", "The most important 3 minutes of the week"); o += 1
    item(d, o, "M01", "3", "8/side", "", "", ""); o += 1
    item(d, o, "M02", "3", "45s/side", "", "", "Tailbone tucked, glute squeezed"); o += 1
    item(d, o, "M03", "2", "5 breaths/side", "", "", ""); o += 1
    item(d, o, "M16", "2", "8/side", "", "", ""); o += 1
    item(d, o, "M04", "2", "6/side", "", "", "Bodyweight, counterweight optional"); o += 1
    item(d, o, "M05", "2", "8/side", "", "", "Bodyweight only"); o += 1
    item(d, o, "M12", "2", "45s/side", "", "", ""); o += 1
    item(d, o, "M14", "3", "10/side", "", "", "Short of symptoms - this is desensitization, not stretching"); o += 1
    item(d, o, "M18", "2", "5 breaths/side", "", "", ""); o += 1
    item(d, o, "M19", "1", "4/side", "", "", "Slow, 10s per rep"); o += 1
    item(d, o, "M11", "2", "10/side", "", "", ""); o += 1
    item(d, o, "M07", "2", "45s", "", "", ""); o += 1
    item(d, o, "C04", "3", "6 (8s holds)", "", "", ""); o += 1
    item(d, o, "C02", "3", "6/side", "", "", ""); o += 1
    item(d, o, "C03", "3", "30s/side", "", "", ""); o += 1
    item(d, o, "M20", "1", "20-30 min", "", "", "Optional but recommended - walking helps nerve symptoms"); o += 1
    return o

def d_long_run(d, km, note, label):
    day(d, "Running - Long", label, "Outdoor")
    o = add_warmup(d, 1, "run")
    item(d, o, "R02", "1", f"{km} km", "", "5:50-6:20 /km", note, km=km); o += 1
    o = add_daily5(d, o)
    return o

def d_off(d, label="Full rest"):
    day(d, "Rest", label, "-")
    item(d, 1, "M20", "1", "20-30 min", "", "", "Easy walk. Nothing else required.")
    item(d, 2, "M08", "2", "5 breaths", "", "", "Optional 5 minutes before bed")

def d_travel_circuit(d, label, rounds=4):
    day(d, "Travel - Circuit", label, "Hotel / park")
    o = 1
    item(d, o, "M08", "2", "5 breaths", "", "", "Warm-up"); o += 1
    item(d, o, "M02", "1", "40s/side", "", "", "Warm-up"); o += 1
    item(d, o, "P03", "2", "20m", "", "", "Warm-up"); o += 1
    item(d, o, "P01", "3", "20 contacts", "45s", "", "Quiet, springy ankles", contacts=60); o += 1
    item(d, o, "P08", "3", "3", "60s", "", "Stick every landing", contacts=9); o += 1
    item(d, o, "S06", str(rounds), "10/side", "60s", "Bodyweight", "Slow 3s down"); o += 1
    item(d, o, "U08", str(rounds), "15", "60s", "Bodyweight", ""); o += 1
    item(d, o, "S12", str(rounds), "12", "60s", "Bodyweight / towel on floor", "Or single-leg glute bridge if no slide surface"); o += 1
    item(d, o, "C01", "3", "8/side", "45s", "", ""); o += 1
    item(d, o, "C03", "3", "30s/side", "30s", "", ""); o += 1
    item(d, o, "S22", "3", "15/side", "45s", "Bodyweight", "Off a step or curb"); o += 1
    o = add_daily5(d, o, "Cool-down mobility")
    return o

def d_travel_mob(d, label="Mobility + walking"):
    day(d, "Travel - Mobility", label, "Hotel / anywhere")
    o = 1
    item(d, o, "M08", "3", "5 breaths", "", "", "Non-negotiable, even on a travel day"); o += 1
    item(d, o, "M01", "2", "8/side", "", "", ""); o += 1
    item(d, o, "M02", "2", "45s/side", "", "", ""); o += 1
    item(d, o, "M03", "2", "5 breaths/side", "", "", ""); o += 1
    item(d, o, "M04", "2", "6/side", "", "", ""); o += 1
    item(d, o, "M14", "2", "10/side", "", "", "Especially after long flights, trains or bus rides"); o += 1
    item(d, o, "C01", "2", "8/side", "", "", ""); o += 1
    item(d, o, "C03", "2", "30s/side", "", "", ""); o += 1
    item(d, o, "M20", "1", "Sightseeing", "", "", "Walking counts. 15k+ steps of sightseeing is real aerobic work."); o += 1
    return o

D = dt.date
# =================================================================== WEEK 1
d_plyo_power(D(2026,9,21), 1,
  [("P23","3 each","max","full","BASELINE TEST. Chalk your standing reach, then test 2-foot and 1-foot approach jumps. Write the numbers down.",6),
   ("P04","3","5","45s","Stick each landing dead still for 2s",15),
   ("P01","3","15","45s","Quiet and springy; contact time is the goal",45)],
  [("S08","3","10","90s","Light - RPE 6","Learn the squeeze, do not arch at the top"),
   ("S16","5","20m","60s","Moderate","Short powerful steps, full hip extension"),
   ("S19","3","12","60s","Moderate","1s pause at the top"),
   ("C01","3","8/side","45s","","")],
  "Baseline test + Plyo intro")
d_run_easy(D(2026,9,22), 32, 4, "Easy 32' + 4 strides")
d_strength(D(2026,9,23),
  [("S06","3","8/side","90s","RPE 6 - bodyweight or light DB","Shin vertical, slow down"),
   ("U01","3","10","90s","RPE 7",""),
   ("U04","3","8-10","90s","Assisted if needed",""),
   ("C05","3","10/side","45s","Light","Ribs down"),
   ("S20","3","15","60s","Moderate",""),
   ("S21","3","20","45s","Bodyweight","")],
  "Strength A - intro")
d_run_quality(D(2026,9,24),
  [("R09","1","6 x 1 min hard / 2 min easy","","By feel, ~5k effort","First quality session back - effort based, ignore the watch",4.5)],
  "Fartlek 6 x 1'")
d_mobility(D(2026,9,25))
d_plyo_power(D(2026,9,26), 1,
  [("P05","4","3","90s","LOW box (12-18in). Land in the same shape you left the ground in",12),
   ("P08","3","3","90s","Stick every landing",9)],
  [("S05","3","8","90s","RPE 6","Goblet - grooving depth and position"),
   ("S09","3","8","90s","LIGHT - RPE 5","Start conservatively; stop at hamstring tension"),
   ("S13","3","12","60s","Bodyweight","Stop at a straight line, do not arch"),
   ("S17","4","20m","60s","Moderate","")],
  "Plyo B + Lower strength")
d_long_run(D(2026,9,27), 7, "Easy and conversational; walk breaks are fine", "Long run 7 km")

# =================================================================== WEEK 2
d_plyo_power(D(2026,9,28), 2,
  [("P04","2","5","45s","",10),
   ("P01","3","18","45s","",54),
   ("P13","2","5/side","60s","Stick the landing 1s each rep",20)],
  [("S02","4","3","2 min","20-25% of trap bar 1RM","Bar speed is the whole point"),
   ("S08","4","8","90s","RPE 7",""),
   ("S16","6","20m","60s","Heavier than last week",""),
   ("S19","4","12","60s","+load","")],
  "Plyo A + Power")
d_run_easy(D(2026,9,29), 38, 5, "Easy 38' + 5 strides")
d_strength(D(2026,9,30),
  [("S06","3","8/side","90s","RPE 7 - add DBs",""),
   ("U01","4","8","90s","RPE 7-8",""),
   ("U05","4","10","75s","RPE 7",""),
   ("C05","3","10/side","45s","",""),
   ("C07","3","30m/side","60s","Heavy","Shoulders level, no lean"),
   ("S20","3","15","60s","",""),
   ("S21","3","20","45s","","")],
  "Strength A")
d_run_quality(D(2026,9,30) + dt.timedelta(days=1),
  [("R05","6","400m","90s standing","1:50-1:56","Even splits. If rep 6 is slower than rep 1, you went out too hard.",2.4)],
  "6 x 400m")
d_mobility(D(2026,10,2))
d_plyo_power(D(2026,10,3), 2,
  [("P05","5","3","90s","Box height +2-4in if landings were clean",15),
   ("P08","3","3","90s","",9),
   ("P11","3","20m","90s","Drive the knee, cover ground",18)],
  [("S01","4","5","2-3 min","RPE 7 - high handles","Main hinge of the block. Push the floor away."),
   ("S11","3","4","90s","3s lower, band assisted","Brutal - ease in"),
   ("S13","3","12","60s","Light load",""),
   ("X06","4","rounds","90s","Moderate sled","Push 20m, drag back 20m")],
  "Plyo B + Heavy lower")
d_long_run(D(2026,10,4), 8, "Steady, comfortable", "Long run 8 km")

# =================================================================== WEEK 3
d_plyo_power(D(2026,10,5), 3,
  [("P01","3","15","45s","",45),
   ("P02","2","15s","45s","As fast as possible on the balls of the feet",30),
   ("P13","2","6/side","60s","",24)],
  [("S02","5","3","2 min","25% 1RM","Fast bar"),
   ("S08","4","8","90s","RPE 7-8",""),
   ("S16","6","20m","60s","Heavy","Strength focus today - slow and grinding is fine"),
   ("S22","3","12/side","60s","","")],
  "Plyo A + Power")
d_run_easy(D(2026,10,6), 38, 5, "Easy 38' + 5 strides")
d_strength(D(2026,10,7),
  [("S07","3","8/side","90s","Knee-height box","No push off the back foot"),
   ("U03","4","6","2 min","RPE 7","Ribs down, glutes squeezed"),
   ("U04","4","6-10","90s","",""),
   ("U07","3","15","45s","Light",""),
   ("C06","3","20s/side","45s","Knee version","Add 5s per week, no more"),
   ("S20","3","15","60s","",""),
   ("S21","3","20","45s","","")],
  "Strength B")
d_run_quality(D(2026,10,8),
  [("R04","4","1000m","90s jog","4:50-5:00 /km","Threshold effort - comfortably hard, not hard",4.0)],
  "4 x 1000m")
d_mobility(D(2026,10,9))
d_plyo_power(D(2026,10,10), 3,
  [("P10","3","5 hurdles","90s","6-8in hurdles. Minimize contact time",15),
   ("P05","5","3","90s","",15),
   ("P12","3","5/side","90s","Tall and reactive",30)],
  [("S01","4","5","2-3 min","RPE 7-8",""),
   ("S09","3","8","90s","RPE 6 - building",""),
   ("S13","3","12","60s","Load",""),
   ("S17","4","20m","60s","Heavy","")],
  "Plyo B + Heavy lower")
d_long_run(D(2026,10,11), 9.5, "Last 10 min may drift faster if it feels natural", "Long run 9.5 km")

# =================================================================== WEEK 4
d_plyo_power(D(2026,10,12), 4,
  [("P01","3","20","45s","",60),
   ("P07","4","3","90s","3s pause in the bottom, then explode - no bounce",12),
   ("P21","4","5","90s","Throw for distance",0)],
  [("S02","5","3","2 min","30% 1RM",""),
   ("S08","4","6","2 min","RPE 8","Heavier, fewer reps"),
   ("S16","6","20m","60s","Heavy",""),
   ("S19","4","10","60s","+load","")],
  "Plyo A + Power")
d_run_easy(D(2026,10,13), 42, 6, "Easy 42' + 6 strides")
d_strength(D(2026,10,14),
  [("S06","4","8/side","90s","RPE 8",""),
   ("U01","4","8","90s","RPE 8",""),
   ("U05","4","10","75s","",""),
   ("C05","3","12/side","45s","",""),
   ("C07","3","40m/side","60s","Heavy",""),
   ("S20","4","15","60s","",""),
   ("S21","3","20","45s","","")],
  "Strength A")
d_run_quality(D(2026,10,15),
  [("R03","1","18 min continuous","","4:55-5:05 /km","Comfortably hard. Lock in and hold.",3.6)],
  "Tempo 18 min")
d_mobility(D(2026,10,16))
d_plyo_power(D(2026,10,17), 4,
  [("P14","4","4","90s","12in box. Land, absorb, FREEZE. No jump.",16),
   ("P05","5","3","90s","",15),
   ("P11","4","20m","90s","",24)],
  [("S01","4","4","3 min","RPE 8",""),
   ("S11","3","4","90s","2s lower, less assistance",""),
   ("S13","3","12","60s","Load",""),
   ("X06","5","rounds","90s","Moderate","")],
  "Plyo B + Heavy lower")
d_long_run(D(2026,10,18), 11, "Fuel beforehand; take water if it is warm", "Long run 11 km")

# =================================================================== WEEK 5
d_plyo_power(D(2026,10,19), 5,
  [("P23","3 each","max","full","CHECK-IN TEST. Same protocol as week 1, fresh.",6),
   ("P17","6","2","90s","Long-low penultimate step, quick last step. Reach with the inside hand.",12),
   ("P01","3","20","45s","",60)],
  [("S02","5","3","2 min","30% 1RM",""),
   ("S08","4","6","2 min","RPE 8",""),
   ("S16","6","20m","60s","Heavy",""),
   ("S22","3","15/side","60s","","")],
  "Vertical check-in + Plyo A")
d_run_easy(D(2026,10,20), 45, 6, "Easy 45' + 6 strides")
d_strength(D(2026,10,21),
  [("S07","4","8/side","90s","Knee height +","" ),
   ("U03","4","6","2 min","RPE 8",""),
   ("U04","4","6-10","90s","Add load if 10 is easy",""),
   ("U07","3","15","45s","",""),
   ("C06","3","30s/side","45s","",""),
   ("S20","4","15","60s","",""),
   ("S21","3","20","45s","","")],
  "Strength B")
d_run_quality(D(2026,10,22),
  [("R04","5","1000m","90s jog","4:50-5:00 /km","Biggest quality session before the trip",5.0)],
  "5 x 1000m")
d_mobility(D(2026,10,23))
d_plyo_power(D(2026,10,24), 5,
  [("P14","4","4","90s","15in box",16),
   ("P10","4","5 hurdles","90s","",20),
   ("P18","6","2","90s","Two-step gather into both feet, then explode",12)],
  [("S01","5","3","3 min","RPE 8-9 - heaviest of the block",""),
   ("S09","3","8","90s","RPE 7",""),
   ("S13","3","12","60s","",""),
   ("S17","4","20m","60s","","")],
  "Plyo B + Peak lower")
d_long_run(D(2026,10,25), 12, "Longest run of the pre-trip block", "Long run 12 km")

# =================================================================== WEEK 6 - departure
d_plyo_power(D(2026,10,26), 6,
  [("P01","3","15","45s","Deload - keep it snappy and short",45),
   ("P05","4","3","90s","",12)],
  [("S08","3","8","90s","RPE 6","Deload week - leave the gym feeling fresh"),
   ("S16","4","20m","60s","Moderate",""),
   ("S19","3","12","60s","","")],
  "Deload - Plyo + Power")
d_run_easy(D(2026,10,27), 30, 4, "Easy 30' + 4 strides (pre-flight)")
d_travel_mob(D(2026,10,28), "FLY YYZ-HKG - in-flight mobility")
rows.append(dict(date=D(2026,10,28), order=0, exid="", name="TRAVEL DAY - Air Canada YYZ to HKG",
                 cat="Note", sets="", reps="", rest="", load="",
                 note="Get up and walk the aisle every 90 min. Do 90/90 hip lifts and nerve glides in the galley - a 15 hour seated flight is the single worst thing you can do to an irritated nerve root.",
                 km=0, contacts=0))
d_travel_mob(D(2026,10,29), "In transit")
d_travel_mob(D(2026,10,30), "Arrive Hong Kong - walk + reset")
d_run_easy(D(2026,10,31), 30, 4, "Easy 30' - Hong Kong")
d_travel_mob(D(2026,11,1), "Travel to Shenzhen")

# =================================================================== WEEK 7 - travel
d_travel_circuit(D(2026,11,2), "Bodyweight circuit A")
d_travel_mob(D(2026,11,3), "Mobility + sightseeing")
d_run_easy(D(2026,11,4), 35, 5, "Easy 35' + strides")
d_travel_mob(D(2026,11,5), "Mobility + sightseeing")
d_travel_circuit(D(2026,11,6), "Bodyweight circuit B")
d_run_quality(D(2026,11,7),
  [("R09","1","8 x 1 min hard / 2 min easy","","~5k effort","Effort based. Any flat stretch of park, promenade or riverside path works.",6.0)],
  "Fartlek 8 x 1'", cd=8)
d_travel_mob(D(2026,11,8), "Mobility + rest")

# =================================================================== WEEK 8 - travel
d_run_easy(D(2026,11,9), 40, 5, "Easy 40' + strides")
d_travel_mob(D(2026,11,10), "Mobility + sightseeing")
d_travel_circuit(D(2026,11,11), "Bodyweight circuit A")
d_travel_mob(D(2026,11,12), "Mobility + sightseeing")
d_run_easy(D(2026,11,13), 40, 6, "Easy 40' + strides")
d_travel_circuit(D(2026,11,14), "Bodyweight circuit B")
d_long_run(D(2026,11,15), 10, "Keep it easy - this is maintenance, not training", "Long run 10 km")

# =================================================================== WEEK 9 - re-entry
d_travel_mob(D(2026,11,16), "Taipei - last mobility day")
d_travel_mob(D(2026,11,17), "FLY TPE-YYZ")
rows.append(dict(date=D(2026,11,17), order=0, exid="", name="TRAVEL DAY - Taipei to Toronto via Seoul",
                 cat="Note", sets="", reps="", rest="", load="",
                 note="Same in-flight rules. Expect 2-3 days of flat legs; do not panic and do not chase the plan.",
                 km=0, contacts=0))
d_run_easy(D(2026,11,18), 30, 4, "Shakeout 30' (jet lag)")
d_strength(D(2026,11,19),
  [("P01","3","15","45s","","Re-introduce ground contact gently"),
   ("S06","3","8/side","90s","RPE 6 - go LIGHTER than you think","3 weeks off means the first session back is deliberately easy"),
   ("S08","3","8","90s","RPE 6",""),
   ("U01","3","10","90s","RPE 7",""),
   ("U05","3","10","75s","",""),
   ("S20","3","15","60s","",""),
   ("S21","3","20","45s","","")],
  "Re-entry strength", "Hyrox gym or GoodLife")
d_mobility(D(2026,11,20))
d_run_quality(D(2026,11,21),
  [("R06","5","800m","2 min jog","3:46 per 800","Goal 10k pace. Learn the feel - you have 2 weeks to make it automatic.",4.0)],
  "5 x 800m @ race pace")
d_long_run(D(2026,11,22), 10, "Rebuild - stay easy", "Long run 10 km")

# =================================================================== WEEK 10 - peak
d_plyo_power(D(2026,11,23), 10,
  [("P01","3","20","45s","",60),
   ("P05","4","3","90s","Moderate box - keep it easy, running is the priority this week",12)],
  [("S08","3","8","90s","RPE 7",""),
   ("S16","5","20m","60s","Moderate",""),
   ("S19","3","12","60s","",""),
   ("C01","3","8/side","45s","","")],
  "Plyo A (reduced) + Power")
d_run_easy(D(2026,11,24), 45, 6, "Easy 45' + 6 strides")
d_strength(D(2026,11,25),
  [("S06","3","6/side","90s","RPE 7","Volume down, quality up - race is 11 days out"),
   ("U01","3","8","90s","",""),
   ("U04","3","8","90s","",""),
   ("C05","3","12/side","45s","",""),
   ("S20","3","15","60s","","")],
  "Strength (reduced volume)")
d_run_quality(D(2026,11,26),
  [("R06","3","2000m","3 min jog","4:42 /km (9:24 per rep)","THE key session. If you can hold this for 3 reps, 47:00 is on.",6.0)],
  "KEY: 3 x 2000m @ race pace", cd=12)
d_mobility(D(2026,11,27))
d_run_easy(D(2026,11,28), 30, 5, "Easy 30' + 5 strides")
d_long_run(D(2026,11,29), 14, "Longest run of the block. Last 3 km at steady effort.", "Long run 14 km")

# =================================================================== WEEK 11 - taper + RACE
day(D(2026,11,30), "Mobility / Rest", "Taper starts - mobility", "Home")
item(D(2026,11,30), 1, "M17", "1", "5 min", "", "", "Taper week: the work is done. Protect it.")
item(D(2026,11,30), 2, "P01", "2", "15", "45s", "", "Just enough to keep the ankles springy", contacts=30)
item(D(2026,11,30), 3, "M08", "3", "5 breaths", "", "", "")
item(D(2026,11,30), 4, "M02", "2", "45s/side", "", "", "")
item(D(2026,11,30), 5, "M01", "2", "8/side", "", "", "")
item(D(2026,11,30), 6, "C01", "2", "8/side", "", "", "")
item(D(2026,11,30), 7, "M14", "2", "10/side", "", "", "")
d_run_easy(D(2026,12,1), 35, 6, "Easy 35' + 6 strides")
d_run_quality(D(2026,12,2),
  [("R06","4","800m","2 min jog","3:46 per 800","Sharpener. Should feel controlled, not hard. Stop if it does not.",3.2)],
  "4 x 800m @ race pace", cd=8)
d_off(D(2026,12,3), "Rest + mobility")
d_run_easy(D(2026,12,4), 25, 4, "Easy 25' + 4 strides")
day(D(2026,12,5), "Rest", "Shakeout + rest", "Outdoor")
item(D(2026,12,5), 1, "R11", "1", "15 min", "", "very easy", "Optional shakeout jog. Legs should feel bouncy, not tired.", km=2.3)
item(D(2026,12,5), 2, "R07", "3", "100m", "walk back", "~85%", "Three easy strides, nothing more", km=0.3)
item(D(2026,12,5), 3, "M08", "2", "5 breaths", "", "", "")
item(D(2026,12,5), 4, "M02", "2", "45s/side", "", "", "Lay out your kit tonight. Eat normally.")
day(D(2026,12,6), "RACE", "10K RACE - goal 47:00", "Race course")
item(D(2026,12,6), 1, "R12", "1", "5 min", "", "", "After 12-15 min easy jog")
item(D(2026,12,6), 2, "R07", "3", "100m", "", "~90%", "Finish the last one 10 min before the gun")
item(D(2026,12,6), 3, "R13", "1", "10 km", "", "4:42 /km target", "First 2 km at goal pace even if it feels too easy. Settle 2-5. Work 5-8. Empty from 8.", km=10)
item(D(2026,12,6), 4, "M20", "1", "15 min", "", "", "Walk, do not sit down immediately")

# =================================================================== WEEK 12 - vertical block
d_off(D(2026,12,7), "Post-race full rest")
d_run_easy(D(2026,12,8), 25, 0, "Recovery jog 25'")
d_strength(D(2026,12,9),
  [("S04","4","5","2-3 min","RPE 7","Running is now maintenance. Jumping is the priority."),
   ("S08","4","8","90s","RPE 8",""),
   ("S06","3","8/side","90s","RPE 7",""),
   ("U01","3","8","90s","",""),
   ("U04","3","8","90s","",""),
   ("S19","4","10","60s","Heavy","")],
  "Strength - vertical block A")
d_plyo_power(D(2026,12,10), 12,
  [("P14","4","4","90s","18in box - clean, frozen landings",16),
   ("P01","3","20","45s","",60),
   ("P17","6","2","2 min","Full approach, max effort",12)],
  [("S02","5","3","2 min","30% 1RM","Speed"),
   ("S16","5","20m","60s","Light and FAST","Speed sled today, not heavy"),
   ("S22","3","15/side","60s","","")],
  "Plyo intensive A")
d_mobility(D(2026,12,11))
d_plyo_power(D(2026,12,12), 12,
  [("P15","4","3","2 min","DEPTH JUMPS. 12in box. Instant rebound - one bounce sound, not a thud.",12),
   ("P18","6","2","2 min","",12),
   ("P20","4","6","60s","",0)],
  [("S01","4","3","3 min","RPE 8",""),
   ("S11","3","5","90s","",""),
   ("S13","3","12","60s","",""),
   ("S19","4","10","60s","Heavy","")],
  "Plyo intensive B + Heavy lower")
d_run_easy(D(2026,12,13), 35, 5, "Easy 35' + 5 strides")

# =================================================================== WEEK 13 - peak + retest
d_plyo_power(D(2026,12,14), 13,
  [("P15","5","3","2 min","15in box",15),
   ("P07","4","3","90s","",12),
   ("P17","8","2","2 min","Quality only - stop when height drops",16)],
  [("S02","5","3","2 min","30-35% 1RM",""),
   ("S08","4","5","2 min","RPE 8-9",""),
   ("S22","3","15/side","60s","","")],
  "Plyo peak A")
d_run_easy(D(2026,12,15), 30, 5, "Easy 30' + 5 strides")
d_strength(D(2026,12,16),
  [("S04","4","3","3 min","RPE 8 - heavy, low volume","Intent on every rep"),
   ("S07","3","6/side","90s","Heavy DBs",""),
   ("U03","3","6","2 min","",""),
   ("U05","3","10","75s","",""),
   ("S19","4","8","60s","Heavy","")],
  "Strength - vertical block B")
d_mobility(D(2026,12,17))
d_plyo_power(D(2026,12,18), 13,
  [("P04","2","5","45s","Primer only",10),
   ("P18","6","2","2 min","",12),
   ("P17","6","2","2 min","Low volume, maximum intent",12)],
  [("S16","4","20m","60s","Light and fast",""),
   ("S22","2","12/side","60s","",""),
   ("C01","2","8/side","45s","","")],
  "Plyo primer (low volume)")
day(D(2026,12,19), "TEST", "RETEST vertical + rim attempts", "Hyrox gym / court")
item(D(2026,12,19), 1, "M17", "1", "5 min", "", "", "Full warm-up - you are testing maximum output")
item(D(2026,12,19), 2, "P03", "2", "20m", "", "", "")
item(D(2026,12,19), 3, "P04", "2", "5", "45s", "", "Primer", contacts=10)
item(D(2026,12,19), 4, "P23", "3 each", "max", "full", "", "FINAL TEST. Standing reach, 2-foot CMJ, 1-foot approach. Compare to Sept 21.", contacts=6)
item(D(2026,12,19), 5, "P17", "8", "2", "2 min", "Max", "Rim attempts. Stop the moment height drops - every rep should be your best.", contacts=16)
item(D(2026,12,19), 6, "M07", "2", "45s", "", "", "")
d_mobility(D(2026,12,20), "Mobility + block review")
item(D(2026,12,20), 0, "R01", "1", "40 min", "", "6:00-6:30 /km",
     "Optional but recommended. Running drops to 2x/week maintenance in this block - do not let it go to zero.", km=6.5)

# contacts for the re-entry pogos (added inside a strength day)
for _r in rows:
    if _r["date"] == D(2026,11,19) and _r["exid"] == "P01":
        _r["contacts"] = 45

