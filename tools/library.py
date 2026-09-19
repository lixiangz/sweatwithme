# Exercise library: id -> (name, category, targets, how_to, default_rx, cautions)

EX = {}

def add(eid, name, cat, targets, how, rx, caution=""):
    EX[eid] = dict(id=eid, name=name, cat=cat, targets=targets, how=how, rx=rx, caution=caution)

# ---------------------------------------------------------------- MOBILITY
C = "Mobility / Prep"
add("M01", "90/90 Hip Switch", C, "Hip internal + external rotation, deep rotators",
    "Sit with both knees bent 90 deg, one leg in front and one to the side. Keep chest tall, rotate both knees over to the other side without using hands. Pause 2s at the end range each side.",
    "2 x 8/side", "Move slow. If you feel a pinch at the front of the hip, sit on a cushion to raise the hips.")
add("M02", "Couch Stretch", C, "Rectus femoris, psoas, anterior hip capsule",
    "Back foot up on a bench or against a wall, front foot flat. Squeeze the glute of the back leg and tuck the tailbone under before leaning up. The tuck is what makes it work.",
    "2 x 45s/side", "Tuck the pelvis first. Arching the lower back to get deeper is exactly what you are trying to fix.")
add("M03", "Half-Kneeling Hip Flexor w/ Overhead Reach", C, "Psoas, QL, lats, t-spine",
    "Half-kneeling, tuck the tailbone, squeeze the down-side glute. Reach the same-side arm overhead and side-bend away. Exhale fully at the end range.",
    "2 x 5 breaths/side", "")
add("M04", "Cossack Squat", C, "Adductors, hip flexion depth, ankle",
    "Wide stance, shift all weight to one side and sit deep, other leg straight with toes up. Hold a light plate at the chest as a counterweight to stay upright.",
    "2 x 6/side", "Keep the heel of the working leg down. Go only as deep as you can without the lower back rounding.")
add("M05", "ATG Split Squat", C, "Hip flexor, VMO, knee flexion tolerance",
    "Long split stance, drop the back knee toward the floor and let the front knee travel forward over the toes. Chest stays up, back heel lifts.",
    "2 x 8/side", "Bodyweight only for the first 4 weeks.")
add("M06", "Frog Stretch", C, "Adductors, medial hip capsule",
    "On forearms and knees, knees wide, shins parallel, feet flexed. Rock the hips back slowly and return. Do not park in the end range.",
    "2 x 8 rocks", "Rock, do not hang out in it.")
add("M07", "Deep Squat Hold (counterweighted)", C, "Hip, knee, ankle flexion; spinal decompression",
    "Hold a 10-15 lb plate at arms length in front, sit into the deepest squat you can with heels down. Use the counterweight to stay upright and relaxed. Breathe.",
    "2 x 45s", "")
add("M08", "90/90 Hip Lift with Breathing", C, "Posterior pelvic tilt, deep core, lumbar reset",
    "Lie on your back, feet flat on a wall or bench with hips and knees at 90 deg. Exhale hard to tilt the pelvis back and flatten the lower back into the floor, then inhale through the nose without losing the tilt.",
    "3 x 5 breaths", "This is the single best reset for the anterior-tilt pattern that is loading your lower back.")
add("M09", "Open Book T-Spine Rotation", C, "Thoracic rotation, pecs",
    "Side-lying, knees stacked on a foam roller, arms out front. Open the top arm and rotate the chest toward the ceiling, keeping the knees pinned down.",
    "2 x 8/side", "Rotation should come from the ribcage, not the lower back.")
add("M10", "Cat-Cow", C, "Segmental spinal mobility",
    "Quadruped. Move one vertebra at a time from full flexion to full extension, timed to the breath.",
    "1 x 10", "")
add("M11", "Ankle Dorsiflexion Wall Drill", C, "Ankle dorsiflexion (directly limits jump depth and running stride)",
    "Toes 4-5 inches from a wall, drive the knee forward over the little toe until it touches the wall without the heel lifting. Back the foot up until it is hard.",
    "2 x 10/side", "Test both sides; the tighter ankle usually matches the tighter hip.")
add("M12", "Banded Lateral Hip Distraction", C, "Hip capsule, joint decompression",
    "Heavy band high around the crease of the hip, step away to create tension, then move into a lunge or rock back on all fours. The band pulls the femur away from the socket.",
    "2 x 45s/side", "")
add("M13", "Supine Figure-4 Stretch", C, "Glute max, piriformis, deep rotators",
    "On your back, ankle across the opposite knee, pull the bottom thigh toward you. Keep the head and shoulders down.",
    "2 x 40s/side", "Gentle only. Cranking on the piriformis can irritate the sciatic nerve running under it.")
add("M14", "Sciatic Nerve Glide (supine)", C, "Sciatic nerve mobility / desensitization",
    "On your back, hip at 90 deg, hold behind the thigh. Straighten the knee while pulling the toes toward you, then bend the knee while pointing the toes. Slow, rhythmic, like flossing.",
    "2 x 10/side", "This should NOT reproduce the tingling. Work in the range just short of any symptom. Never stretch into it.")
add("M15", "Hip Airplane", C, "Hip rotation control under load, glute med",
    "Stand on one leg holding a support, hinge forward to a T. Rotate the pelvis open and closed over the planted femur while the torso stays still.",
    "2 x 6/side", "Start with a hand on a rack.")
add("M16", "Adductor Rock Back", C, "Adductors, hip flexion pattern",
    "Quadruped, one leg extended straight out to the side with the foot flat. Rock the hips back toward the heel.",
    "2 x 8/side", "")
add("M17", "Foam Roll Circuit", C, "Quads, glutes, lats, calves, t-spine",
    "60-90s per area: quads, glute/TFL, lats, calves. Then lie back over the roller across the mid-back and extend over it for 10 slow breaths.",
    "5-6 min", "Skip direct rolling on the lower back itself; roll the hips and t-spine instead.")
add("M18", "Bretzel Stretch", C, "Quad, hip flexor, t-spine rotation combined",
    "Side-lying, bottom leg bent back and held by the top hand, top leg bent forward and pinned by the bottom hand. Rotate the shoulders back toward the floor and breathe.",
    "2 x 5 breaths/side", "")
add("M19", "Standing Hip CARs", C, "Full hip joint control through range",
    "Stand tall holding support. Lift one knee to the chest, circle it out to the side, rotate back and extend behind you, then return. Slow and deliberate, 10s per rep.",
    "1 x 4/side", "")
add("M20", "Walk / Easy Spin (active recovery)", C, "Circulation, symptom management",
    "Easy walk outdoors or 15 min very light bike. Nothing that raises breathing much.",
    "20-30 min", "Walking is one of the better things you can do for nerve-related back symptoms.")

# ---------------------------------------------------------------- CORE
C = "Core / Spine"
add("C01", "Dead Bug", C, "Anti-extension core, deep abdominals",
    "On your back, arms up and hips/knees at 90. Press the lower back into the floor, then lower the opposite arm and leg slowly while keeping it pressed. Exhale on the way down.",
    "3 x 8/side", "The moment the lower back lifts off the floor, you have gone too far.")
add("C02", "Bird Dog", C, "Anti-rotation, spinal endurance, glutes",
    "Quadruped, extend opposite arm and leg to a straight line. Hold 5-8s. Keep the hips level - put a light object on the lower back to check.",
    "3 x 6/side", "")
add("C03", "Side Plank", C, "Quadratus lumborum, obliques, glute med",
    "Forearm and knees (or feet) supported, body in a straight line, hips stacked and pushed forward. Brace as if about to be punched.",
    "3 x 30s/side", "Progress from knees to feet before adding time.")
add("C04", "McGill Curl-Up", C, "Rectus abdominis without spinal flexion",
    "One knee bent, one straight. Hands under the lower back to preserve its arch. Lift only the head and shoulders an inch off the floor. Do not flatten the back.",
    "3 x 6 (8s holds)", "Designed specifically for backs that do not tolerate crunches.")
add("C05", "Pallof Press", C, "Anti-rotation, obliques, core stiffness",
    "Stand side-on to a cable or band at chest height. Press the handle straight out and resist the rotational pull. Ribs down.",
    "3 x 10/side", "")
add("C06", "Copenhagen Plank", C, "Adductors, groin strength",
    "Side plank with the top leg on a bench, bottom leg hanging. Lift the bottom leg to meet the bench. Start with the knee on the bench, not the ankle.",
    "3 x 20s/side", "Very effective but very easy to overdo. Add 5s per week.")
add("C07", "Suitcase Carry", C, "Anti-lateral-flexion, grip, QL",
    "Heavy dumbbell or kettlebell in one hand only. Walk tall, shoulders level, no lean. Switch sides.",
    "3 x 30m/side", "")
add("C08", "Hollow Body Hold", C, "Anterior chain, total body tension",
    "On your back, lower back pressed down, arms and legs extended and lifted just off the floor. Lower the limbs only as far as the back stays flat.",
    "3 x 20s", "")
add("C09", "Glute Bridge March", C, "Glute endurance, pelvic control",
    "Bridge up and hold. March one knee up without letting the hips dip or rotate.",
    "3 x 8/side", "")

# ---------------------------------------------------------------- PLYO
C = "Plyometric / Jump"
add("P01", "Pogo Hops", C, "Ankle stiffness, achilles elasticity, reactive strength",
    "Stiff legs, minimal knee bend, bounce off the balls of the feet. Aim for minimum ground contact time, not maximum height. Think of the ankles as springs.",
    "3 x 20 contacts", "The single highest-return low-risk jump drill. Quiet landings.")
add("P02", "Line Hops / Ankling", C, "Foot-ankle reactivity, coordination",
    "Hop forward and back or side to side over a line as fast as possible, staying on the balls of the feet.",
    "3 x 15s", "")
add("P03", "A-Skip", C, "Running mechanics, hip flexion, ground stiffness",
    "Skip driving one knee to hip height with a dorsiflexed foot, then strike down and back under the hip. Tall posture, arms driving.",
    "3 x 20m", "")
add("P04", "Snap-Down (Drop and Stick)", C, "Landing mechanics, eccentric absorption",
    "Stand tall on the toes, then snap down fast into a quarter-squat athletic position and freeze. You are training how to absorb force, which comes before producing it.",
    "3 x 5", "Stick every rep dead still for 2s. This is the prerequisite for all box and depth work.")
add("P05", "Box Jump (step down)", C, "Concentric hip/knee extension power, triple extension",
    "Load into a quarter squat, swing the arms, jump onto the box and land softly in the same quarter-squat shape. Step down, never jump down.",
    "5 x 3", "Box height should let you land in the same position you took off from. Tucking the knees to your chest to clear a taller box is ego, not training.")
add("P06", "Countermovement Vertical Jump", C, "Max vertical, stretch-shortening cycle",
    "Two feet, quick dip to a comfortable depth, arms swing hard and up. Reach with one hand at the top to a fixed target. Full reset between reps.",
    "5 x 3", "Quality only. Stop the set the moment height drops.")
add("P07", "Squat Jump (non-countermovement)", C, "Pure concentric power, rate of force development",
    "Sink to a quarter squat, hold for a full 3s to kill the stretch reflex, then jump as high as possible. No bounce.",
    "4 x 3", "Exposes concentric weakness that the bounce hides.")
add("P08", "Broad Jump", C, "Horizontal power, hip extension",
    "Two feet, swing arms back, jump as far forward as possible, land soft in a squat and stick it.",
    "4 x 3", "Stick each landing. Do not do these for continuous reps early on.")
add("P09", "Tuck Jump", C, "Reactive strength, hip flexor speed",
    "Continuous jumps pulling the knees toward the chest, landing and rebounding immediately.",
    "3 x 6", "Fatiguing and high impact - keep sets short.")
add("P10", "Hurdle Hop (continuous)", C, "Reactive strength, ankle/knee stiffness",
    "Line up 4-6 low hurdles or boxes. Hop over each with both feet, minimizing ground contact time between them.",
    "4 x 5 hurdles", "Start at 6-8 inches. Height matters far less than contact time.")
add("P11", "Alternating Bound", C, "Single-leg power, horizontal force, stride power",
    "Exaggerated running leaps, driving the knee up and covering as much ground per stride as possible. Arms drive opposite.",
    "4 x 20m", "")
add("P12", "Single-Leg Hop (linear)", C, "Unilateral reactive strength, ankle stiffness",
    "Continuous hops forward on one leg, staying tall and reactive off the ball of the foot.",
    "3 x 8/side", "Do these before you ever attempt one-foot approach jumps at height.")
add("P13", "Lateral Bound (Skater)", C, "Frontal plane power, glute med, hip stability",
    "Push off one leg laterally, land on the other, stick for 1s, then bound back. Land with the knee tracking over the foot.",
    "3 x 6/side", "")
add("P14", "Depth Drop (landing only)", C, "Eccentric absorption, landing stiffness",
    "Step off a 12-18 inch box, land on both feet in an athletic quarter-squat and freeze. No jump.",
    "4 x 4", "The mandatory precursor to depth jumps. Two weeks of these before adding the rebound.")
add("P15", "Depth Jump", C, "Reactive strength, stretch-shortening cycle, max power",
    "Step off a 12-18 inch box, and the instant you touch the ground jump as high as possible. Ground contact should be under 0.25s - it should sound like one bounce, not a thud and a push.",
    "4 x 3", "Advanced. Only after depth drops are clean. Full 2 min rest between sets. Never on tired legs.")
add("P16", "Seated Box Jump", C, "Pure concentric power from a dead stop",
    "Sit on a box, feet planted. Without rocking, explode up onto a box in front of you.",
    "4 x 3", "")
add("P17", "One-Foot Approach Jump", C, "Basketball-specific max vertical, penultimate step",
    "3-4 step approach. The second-to-last step is long and low (the penultimate step), the last is quick - convert horizontal speed into vertical. Reach with the inside hand.",
    "6 x 2", "Most people jump 3-5 inches higher off one foot with an approach. This is your fastest route to the rim.")
add("P18", "Two-Foot Approach Jump", C, "Max vertical off two feet, power step",
    "2-3 step approach into a hop that lands both feet simultaneously, then immediate explosive jump. Arms swing back on the gather and up hard on takeoff.",
    "6 x 2", "")
add("P19", "Split Jump (Scissor)", C, "Single-leg power, hip flexor/extensor speed",
    "Lunge position, jump and switch legs in the air, landing softly in the opposite lunge.",
    "3 x 8/side", "")
add("P20", "Med Ball Slam", C, "Total body power, lat and core expression",
    "Reach the ball overhead with full extension, then slam it down as hard as possible, following through into a hinge.",
    "4 x 6", "Hinge at the hips, do not round the lower back to reach the floor.")
add("P21", "Med Ball Overhead Backward Throw", C, "Triple extension power, posterior chain",
    "Hold the ball low between the legs, then explosively extend hips, knees and ankles and throw it back over your head as far as possible.",
    "4 x 5", "One of the purest measures of triple extension. Throw for distance.")
add("P22", "Med Ball Rotational Throw", C, "Rotational power, obliques",
    "Side-on to a wall, rotate through the back hip and fire the ball into the wall. Power comes from the hips, not the arms.",
    "3 x 6/side", "")
add("P23", "Vertical Jump Test", C, "Benchmark",
    "Measure standing reach against a wall with chalk. Then take 3 max countermovement jumps and 3 max one-foot approach jumps, marking the highest touch. Record the difference.",
    "3 attempts each", "Test fresh, at the start of a session, never at the end.")

# ---------------------------------------------------------------- LOWER STRENGTH
C = "Lower Body Strength"
add("S01", "Trap Bar Deadlift", C, "Glutes, quads, hamstrings, total posterior chain",
    "High handles to start. Hips slightly higher than a squat, chest up, push the floor away. The trap bar keeps the load in line with your body instead of in front of it.",
    "4 x 5", "Far kinder to the lower back than a conventional pull. This is your main hinge for the whole block.")
add("S02", "Trap Bar Jump", C, "Rate of force development, triple extension under load",
    "Light load (20-30% of your trap bar 1RM). Dip and jump, leaving the ground a few inches. Reset each rep.",
    "5 x 3", "Speed is the point. If the bar is slow, it is too heavy.")
add("S03", "Back Squat", C, "Quads, glutes, spinal erectors",
    "Bar on the upper traps, brace hard, sit between the hips to depth, drive up without letting the hips shoot back first.",
    "4 x 5", "If the tingling shows up under the bar, switch to front or goblet squats for a few weeks.")
add("S04", "Front Squat / Safety-Bar Squat", C, "Quads, upper back, trunk - lower spinal shear than back squat",
    "Elbows high, bar resting on the front delts (or safety bar handles forward). Upright torso, sit straight down.",
    "4 x 5", "The more upright torso puts less extension demand on the lower back. Preferred while symptoms are present.")
add("S05", "Goblet Squat", C, "Quads, glutes, trunk, squat depth",
    "Dumbbell or kettlebell held at the chest, elbows inside the knees at the bottom. Sit straight down between the heels.",
    "3 x 10", "")
add("S06", "Bulgarian Split Squat", C, "Quads, glutes, hip stability, single-leg strength",
    "Rear foot on a bench, front foot far enough forward that the shin stays near vertical. Drop straight down, drive through the whole front foot.",
    "3 x 8/side", "The highest-value lower body exercise for jumping that is not a jump. Also spares the spine.")
add("S07", "High Box Step-Up", C, "Glutes, quads, single-leg drive, hip extension power",
    "Box at or just above knee height. Place the whole foot on the box, drive up through the heel without pushing off the back foot. Lower under control.",
    "3 x 8/side", "Resist bouncing off the trailing leg - that is where the exercise gets cheated.")
add("S08", "Barbell Hip Thrust", C, "Glute max at end range hip extension",
    "Shoulder blades on a bench, bar across the hips on a pad, feet flat and shins vertical at the top. Drive the hips up, tuck the ribs down, squeeze hard for 1s.",
    "4 x 8", "Do not hyperextend the lower back at the top - the range should come from the hips.")
add("S09", "Romanian Deadlift", C, "Hamstrings, glutes, posterior chain",
    "Soft knees, push the hips straight back, bar stays in contact with the legs. Stop when the hamstrings reach tension or the back starts to round, whichever is first.",
    "3 x 8", "Start light given the nerve symptoms - loaded hamstring tension can provoke them. Build slowly.")
add("S10", "Single-Leg RDL", C, "Hamstring, glute, balance, hip control",
    "One leg planted, hinge forward while the other leg extends behind, hips square. Light dumbbell in the opposite hand.",
    "3 x 8/side", "")
add("S11", "Nordic Hamstring Curl (eccentric)", C, "Hamstring eccentric strength, injury resistance",
    "Kneel with ankles anchored. Lower as slowly as possible under control, catch with the hands, push back up.",
    "3 x 4", "The best known hamstring injury preventer. Brutally hard - start with a 3s lower and band assistance.")
add("S12", "Hamstring Slider Curl", C, "Hamstrings at the knee, glutes",
    "Bridge position with heels on sliders or a towel. Extend the legs out keeping the hips up, then pull the heels back in.",
    "3 x 10", "")
add("S13", "45-Degree Back Extension", C, "Glutes and hamstrings, spinal erector endurance",
    "Pad just below the hip crease. Round slightly or stay neutral, hinge down and drive up with the glutes, stopping at a straight line.",
    "3 x 12", "Stop at straight. Do not arch past neutral at the top.")
add("S14", "Kettlebell Swing", C, "Explosive hip extension, glutes, hamstrings, conditioning",
    "Hinge, hike the bell back behind you, then snap the hips forward. The bell floats - the arms do nothing. Stand fully tall at the top.",
    "5 x 12", "A hinge and a snap, not a squat and a lift.")
add("S15", "Reverse Lunge (DB)", C, "Quads, glutes, single-leg control",
    "Step back into a lunge, drop the back knee toward the floor, drive back through the front heel. Easier on the knees than a forward lunge.",
    "3 x 8/side", "")
add("S16", "Sled Push", C, "Glutes, quads, calves, horizontal force production, conditioning",
    "Low arms, body at a forward angle, drive with short powerful steps and full hip extension. Heavy = strength, light = speed.",
    "6 x 20m", "Zero spinal compression and zero eccentric load. As close to a free lunch as training offers for a cranky back.")
add("S17", "Backward Sled Drag", C, "VMO, quads, knee health",
    "Strap or handles, walk backward leaning slightly back, taking short steps and extending the knee fully each step.",
    "4 x 20m", "Excellent for knee resilience once you start loading jumps.")
add("S18", "Lateral Band Walk", C, "Glute medius, hip abductors",
    "Band above the knees or at the ankles, quarter squat, step sideways keeping tension the whole time. Toes forward.",
    "3 x 12/side", "")
add("S19", "Standing Calf Raise", C, "Gastrocnemius, achilles stiffness",
    "Full range - all the way down for a stretch, all the way up onto the big toe. Pause 1s at the top.",
    "4 x 12", "Calves are the last link in the jump chain and the most commonly under-trained.")
add("S20", "Seated Calf Raise", C, "Soleus (the muscle that matters most for running)",
    "Knees bent at 90, full range, slow 2s lower and 1s pause at the top.",
    "3 x 15", "The soleus takes more load per stride than any other muscle while running.")
add("S21", "Tibialis Raise", C, "Tibialis anterior, shin splint resistance, ankle balance",
    "Heels against a wall, lean back, lift the toes toward the shins as high as possible and lower slowly.",
    "3 x 20", "Cheap insurance as running volume climbs.")
add("S22", "Single-Leg Calf Raise", C, "Unilateral calf strength and stiffness",
    "One leg, off a step for full range, hold a support for balance only.",
    "3 x 12/side", "Aim to work toward 20+ clean reps per side.")
add("S23", "Leg Press", C, "Quads and glutes with no spinal load",
    "Feet mid-platform, control the descent to about 90 degrees of knee bend, do not let the lower back round off the pad at the bottom.",
    "3 x 10", "Useful substitute on days the back is irritable.")

# ---------------------------------------------------------------- UPPER
C = "Upper Body"
add("U01", "Dumbbell Bench Press", C, "Chest, front delts, triceps",
    "Feet planted, slight arch, lower to the chest under control, press without letting the elbows flare to 90.",
    "4 x 8", "")
add("U02", "Incline DB Press", C, "Upper chest, front delts",
    "Bench at 30 degrees, same pattern as flat pressing.",
    "3 x 10", "")
add("U03", "Overhead Press", C, "Shoulders, triceps, trunk",
    "Standing, brace the trunk and squeeze the glutes, press straight overhead and finish with the biceps by the ears.",
    "4 x 6", "Ribs down. Leaning back to press is a lower-back cost you do not need.")
add("U04", "Pull-Up / Lat Pulldown", C, "Lats, upper back, biceps",
    "Full hang to chin over the bar. Pull the elbows down and back, do not shrug.",
    "4 x 6-10", "")
add("U05", "Chest-Supported Row", C, "Mid-back, rhomboids, rear delts",
    "Chest on an incline bench, row the dumbbells toward the hips, squeeze the shoulder blades.",
    "4 x 10", "Chest support takes the lower back entirely out of it.")
add("U06", "Single-Arm DB Row", C, "Lats, mid-back, anti-rotation",
    "One hand and knee on the bench, flat back, row toward the hip.",
    "3 x 10/side", "")
add("U07", "Face Pull", C, "Rear delts, external rotators, posture",
    "Rope at face height, pull toward the forehead with the elbows high, finish with the hands wide.",
    "3 x 15", "Direct antidote to the desk posture.")
add("U08", "Push-Up", C, "Chest, triceps, trunk",
    "Rigid plank from heels to head, elbows about 45 degrees to the body.",
    "3 x 12-20", "")
add("U09", "Dip", C, "Chest, triceps, front delts",
    "Slight forward lean, lower until the upper arms are parallel, press up without locking hard.",
    "3 x 8", "")

# ---------------------------------------------------------------- RUNNING
C = "Running"
add("R01", "Easy Run", C, "Aerobic base, capillary density, fat oxidation",
    "Conversational the entire time. If you cannot speak a full sentence, slow down. Target 6:00-6:30 /km.",
    "35-50 min", "Roughly 80% of your weekly running should live here. Running easy days too hard is the most common reason people plateau.")
add("R02", "Long Run", C, "Aerobic endurance, connective tissue, fuel efficiency",
    "Steady and comfortable, 5:50-6:20 /km. Last 10 minutes may drift faster if it feels natural.",
    "8-16 km", "Build no more than about 1.5 km per week.")
add("R03", "Tempo / Threshold Run", C, "Lactate threshold, race-specific endurance",
    "Continuous effort at 4:55-5:05 /km. Comfortably hard - you could speak 3-4 words, not a sentence. 10 min easy either side.",
    "15-25 min", "The highest-return single session for a 10k.")
add("R04", "1000m Cruise Intervals", C, "Threshold + speed endurance",
    "1000m reps at 4:50-5:00 /km with 90s easy jog between. Even splits - the last rep should match the first.",
    "4-6 x 1000m", "")
add("R05", "400m Repeats", C, "VO2max, running economy, leg speed",
    "400m at 1:46-1:52 with 90s standing/walking rest. Relaxed face and shoulders, fast legs.",
    "6-10 x 400m", "Your old peak set was 9x400. That is the benchmark to chase back.")
add("R06", "800m Repeats @ Race Pace", C, "10k-specific pacing, race rehearsal",
    "800m at goal 10k pace (3:46 per 800 for a 47:00 finish) with 2 min jog recovery. Learn what the pace feels like.",
    "5-6 x 800m", "")
add("R07", "Strides", C, "Neuromuscular speed, running mechanics",
    "100m accelerations building to about 90% over the first 40m, hold relaxed, then decelerate. Full walk-back recovery.",
    "4-6 x 100m", "Not a sprint. These stay fresh and sharp - add them after easy runs.")
add("R08", "Hill Sprints", C, "Power, running-specific strength, tendon stiffness",
    "Steep hill, 10-12 seconds all out from a standing start, walk down fully (2-3 min). Tall posture, drive the knees.",
    "6-10 reps", "Doubles as jump training and is far lower impact than flat sprinting.")
add("R09", "Fartlek", C, "Aerobic power, pacing feel",
    "Within an easy run, alternate 1 min hard / 2 min easy. Unstructured effort by feel, not by watch.",
    "6-10 x 1 min", "")
add("R10", "Progression Run", C, "Pacing discipline, fatigue resistance",
    "Split the run into thirds: easy, steady, then moderately hard. Never start fast.",
    "40-60 min", "")
add("R11", "Recovery Jog / Shakeout", C, "Blood flow, recovery",
    "Very easy, 6:30+ /km. Short. The goal is to feel better afterward than before.",
    "20-25 min", "")
add("R12", "Run Drills (warm-up)", C, "Mechanics, hip mobility, preparation",
    "A-skips, B-skips, high knees, butt kicks, carioca, leg swings - 20m each.",
    "5-6 min", "Do these before every quality session.")
add("R13", "10K RACE", C, "The day",
    "Warm up 15 min easy plus drills and 3 strides. Go out at goal pace for the first 2 km even if it feels slow. Settle. Work from 5k. Empty the tank from 8k.",
    "10 km", "The first kilometre run 15s too fast costs you a minute later.")

# ---------------------------------------------------------------- CONDITIONING
C = "Conditioning / Hyrox"
add("X01", "SkiErg Intervals", C, "Aerobic power, lats, trunk - zero impact",
    "500m repeats at a hard but repeatable pace with 90s rest. Hinge and drive with the trunk, not just the arms.",
    "5 x 500m", "Great way to add aerobic work without adding pounding to the legs.")
add("X02", "Rowing Intervals", C, "Aerobic power, posterior chain, no impact",
    "500m repeats, 90s rest. Legs-hips-arms on the drive, reverse on the recovery.",
    "5 x 500m", "Keep the back neutral; rowing with a rounded spine under fatigue is a common irritant.")
add("X03", "Assault Bike Intervals", C, "Aerobic power, zero impact",
    "30s hard / 60s easy, or 60s hard / 60s easy for a longer piece.",
    "8-10 rounds", "The safest way to get your heart rate high when the legs are beaten up.")
add("X04", "Wall Balls", C, "Quads, glutes, shoulders, conditioning",
    "Full squat depth, drive up and throw to the target, catch and absorb into the next squat.",
    "4 x 20", "")
add("X05", "Farmer Carry Intervals", C, "Grip, traps, trunk, posture under load",
    "Heavy carries for distance, walking tall with the shoulders back.",
    "4 x 40m", "")
add("X06", "Sled Push-Pull Circuit", C, "Full body conditioning with no eccentric damage",
    "Push 20m, turn and drag backward 20m. That is one round. Rest 60-90s.",
    "6 rounds", "The best conditioning option on the list for someone protecting their lower back.")
add("X07", "Hyrox Compromised-Run Block", C, "Running under fatigue, hybrid capacity",
    "1000m run, then a station (sled push, burpee broad jumps, or wall balls), repeat. Runs stay honest, stations stay unbroken.",
    "3-4 rounds", "")
