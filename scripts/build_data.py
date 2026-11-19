"""Rebuild the dashboard's annual CMA data from original quarterly CSV files.

Usage: python scripts/build_data.py
Python 3.9+; standard library only.
Required inputs: data/raw/ow_cma.csv, odsp_cma.csv, cma_population_2005_2025.csv.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
CODES = (505, 521, 529, 532, 535, 537, 539, 541, 543, 550, 555, 559, 568, 580, 595)
YEARS = range(2005, 2026)
OW_FIELDS = ("cases", "fts", "ftsp", "ftc", "age24", "age2554", "age55", "moa04", "moa512", "moa1318", "moa19")
ODSP_FIELDS = ("cases", "fts", "ftsp", "ftc", "age24", "age2554", "age55", "moa035", "moa3659", "moa60")

def read_csv(name):
    with (RAW / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def annual_cases(filename, fields):
    buckets = defaultdict(list)
    for row in read_csv(filename):
        code, year = int(row["cma_code"]), int(row["year"])
        if code in CODES and year in YEARS:
            buckets[(code, year)].append(row)
    output = {}
    for key, rows in buckets.items():
        if len(rows) != 4 or sorted(int(r["month"]) for r in rows) != [3, 6, 9, 12]:
            raise ValueError(f"{filename}: expected four quarterly records for {key}")
        output[key] = {field: mean(float(r[field]) for r in rows) for field in fields}
    return output

def population():
    output = {}
    for row in read_csv("cma_population_2005_2025.csv"):
        dguid = row["DGUID"]
        if not dguid or not (dguid.startswith("2021S0503") or dguid == "2021S050535505"):
            continue
        code, year = int(dguid[-3:]), int(row["REF_DATE"])
        if code == 505 and "Ontario part" not in row["GEO"]:
            continue
        if code in CODES and year in YEARS and row["Gender"] == "Total - gender" and row["Age group"] == "All ages":
            key = (code, year)
            if key in output:
                raise ValueError(f"Duplicate population record: {key}")
            output[key] = float(row["VALUE"])
    return output

def main():
    ow = annual_cases("ow_cma.csv", OW_FIELDS)
    odsp = annual_cases("odsp_cma.csv", ODSP_FIELDS)
    pop = population()
    expected = {(code, year) for code in CODES for year in YEARS}
    for name, records in (("OW", ow), ("ODSP", odsp), ("population", pop)):
        if set(records) != expected:
            raise ValueError(f"{name}: missing {sorted(expected - set(records))}; extra {sorted(set(records) - expected)}")
    result = {
        f"{code}-{year}": {
            "code": code, "year": year, "population": pop[(code, year)],
            "ow": ow[(code, year)], "odsp": odsp[(code, year)]
        }
        for code in CODES for year in YEARS
    }
    output = ROOT / "real_data.json"
    output.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {len(result)} CMA-year records to {output}")

if __name__ == "__main__":
    main()
