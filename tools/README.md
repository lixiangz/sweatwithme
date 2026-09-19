# Regenerating the plan

`library.py` holds every exercise (name, targets, how-to, cautions).
`plan.py` builds all 91 days from those exercises.
`gen_plan_json.py` writes `../src/data/plan.json`.

```bash
cd tools && python3 gen_plan_json.py
```

Change a session in `plan.py` or an exercise in `library.py`, rerun, rebuild.
The same two files also generate the Excel workbook.
