import json, datetime as dt
import plan as P
from library import EX

START = dt.date(2026, 9, 21)

BLOCKS = {1: "Foundation", 2: "Foundation", 3: "Foundation", 4: "Build", 5: "Build",
          6: "Travel", 7: "Travel", 8: "Travel", 9: "Race sharpening",
          10: "Race sharpening", 11: "Race sharpening", 12: "Vertical peak", 13: "Vertical peak"}

BLOCK_NO = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 5, 13: 5}

SECTION_FOR_CAT = {
    "Plyometric / Jump": "Jumps",
    "Lower Body Strength": "Strength",
    "Upper Body": "Strength",
    "Running": "Running",
    "Conditioning / Hyrox": "Conditioning",
    "Core / Spine": "Core",
    "Mobility / Prep": "Mobility",
    "Note": "Note",
}

PREP = {"Mobility / Prep", "Core / Spine"}


def sections_for(items):
    """Leading prep run -> Warm-up, trailing prep run -> Cool-down, middle by category."""
    n = len(items)
    if n == 0:
        return []
    lead = 0
    while lead < n and items[lead]["cat"] in PREP:
        lead += 1
    # a lone A-skip at the end of the warm-up belongs to it
    if lead < n and items[lead]["exid"] == "P03":
        lead += 1
    tail = n
    while tail > lead and items[tail - 1]["cat"] in PREP:
        tail -= 1

    out = []
    if lead > 0:
        out.append({"title": "Warm-up", "accent": "olive", "items": items[0:lead]})
    cur, curname = [], None
    for it in items[lead:tail]:
        nm = SECTION_FOR_CAT.get(it["cat"], "Main")
        if nm != curname:
            if cur:
                out.append({"title": curname, "accent": ACCENT.get(curname, "text"), "items": cur})
            cur, curname = [], nm
        cur.append(it)
    if cur:
        out.append({"title": curname, "accent": ACCENT.get(curname, "text"), "items": cur})
    if tail < n:
        out.append({"title": "Cool-down", "accent": "grey", "items": items[tail:n]})
    return out


ACCENT = {"Jumps": "orange", "Strength": "olive", "Running": "teal",
          "Conditioning": "teal", "Core": "olive", "Mobility": "grey", "Note": "orange"}

FOCUS_ACCENT = {
    "Plyo / Power": "orange", "Running - Easy": "teal", "Running - Quality": "teal",
    "Running - Long": "teal", "Strength": "olive", "Mobility / Rest": "grey",
    "Rest": "grey", "Travel - Circuit": "orange", "Travel - Mobility": "grey",
    "RACE": "red", "TEST": "orange",
}

by_date = {}
for r in P.rows:
    by_date.setdefault(r["date"], []).append(r)

days = []
d = START
while d <= dt.date(2026, 12, 20):
    wk = (d - START).days // 7 + 1
    m = P.daymeta[d]
    items = []
    for r in sorted(by_date.get(d, []), key=lambda r: r["order"]):
        items.append({
            "exid": r["exid"], "name": r["name"], "cat": r["cat"],
            "sets": r["sets"], "reps": r["reps"], "rest": r["rest"],
            "load": {"Load": "Add load", "+load": "Add load"}.get(r["load"], r["load"]),
            "note": r["note"],
            "km": r["km"], "contacts": r["contacts"],
        })
    days.append({
        "date": d.isoformat(),
        "dow": d.strftime("%A"),
        "week": wk,
        "block": BLOCK_NO[wk],
        "blockName": BLOCKS[wk],
        "focus": m["focus"],
        "accent": FOCUS_ACCENT.get(m["focus"], "grey"),
        "label": m["label"],
        "location": m["location"],
        "km": round(sum(i["km"] for i in items), 1),
        "contacts": sum(i["contacts"] for i in items),
        "sections": sections_for(items),
    })
    d += dt.timedelta(days=1)

# only the exercises actually referenced
used = sorted({i["exid"] for day in days for s in day["sections"] for i in s["items"] if i["exid"]})
exercises = {e: {"name": EX[e]["name"], "cat": EX[e]["cat"], "targets": EX[e]["targets"],
                 "how": EX[e]["how"], "rx": EX[e]["rx"], "caution": EX[e]["caution"]}
             for e in used}

out = {
    "meta": {
        "title": "Hybrid block",
        "start": START.isoformat(),
        "end": "2026-12-20",
        "weeks": 13,
        "race": {"name": "10K Race", "date": "2026-12-06", "goal": "47:00", "pace": "4:42 /km"},
        "travel": {"from": "2026-10-28", "to": "2026-11-17"},
        "generated": dt.date.today().isoformat(),
    },
    "exercises": exercises,
    "days": days,
}

with open("../src/data/plan.json", "w") as f:
    json.dump(out, f, separators=(",", ":"), ensure_ascii=False)

print("days:", len(days), "exercises:", len(exercises))
print("sample sections:", [s["title"] for s in days[19]["sections"]], days[19]["label"])
