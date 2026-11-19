# The Changing Face of Social Assistance

**Live interactive dashboard:** https://annieqiulq.github.io/sta313-social-assistance-dashboard/

An interactive policy-oriented visualization of Ontario Works (OW) and Ontario Disability Support Program (ODSP) caseload rates across 15 Ontario census metropolitan areas (CMAs), 2005–2025.

## How to explore
The **Focus** view provides a larger map for examining one CMA; **Overview** compresses the coordinated charts so analysts can compare places and change periods with less scrolling. These display modes use the same data and selections.

1. Select the **start and end years** and choose **OW**, **ODSP**, or **OW + ODSP**.
2. Compare percentage changes in the **CMA map** and **ranked bar chart**. Click a CMA dot or ranking row to select it; the policy readout updates with the selected CMA's rate change and comparative rank.
3. Read the selected CMA's **2005–2025 historical trend** (the complete timeline remains visible when the period changes).
4. Use **Household type**, **Age**, and **Time on assistance** to investigate which groups contributed to changes in annual-average case counts.

The map's dot size is constant; dot colour encodes percentage change in the selected caseload rate. The ranking uses the same measure and palette. The breakdown chart reports percentage contributions relative to the starting annual-average program caseload, **not** percentage-point changes in population-normalized rates.

## Data and reproducibility
The dashboard loads `real_data.json`, which contains **315 CMA-year observations** (15 CMAs × 21 years). `scripts/build_data.py` reproduces it from three source CSVs:

- `ont-sa-characteristic-ow-cma.csv`: quarterly Ontario Works CMA caseload characteristics, Ontario Ministry of Children, Community and Social Services.
- `ont-sa-characteristic-odsp-cma.csv`: quarterly ODSP CMA caseload characteristics, same ministry.
- `2005-2025-cma-population.csv`: annual Statistics Canada CMA population, 2021 CMA geography, all ages and total gender.

**Reproducibility:** All three original source CSVs are committed in the repository root. The script reads them directly, so no file moves or renames are required.

To rebuild the dashboard dataset from the committed source CSVs, run:

```bash
python scripts/build_data.py
```

The script uses only the Python standard library, validates four quarterly observations per CMA-year and complete 2005–2025 coverage, and writes `real_data.json`.

**Definitions:** Annual cases = arithmetic mean of March, June, September and December case counts. Caseload rate = annual-average cases ÷ annual CMA population × 1,000. Percentage change = (end rate ÷ start rate − 1) × 100. Ottawa–Gatineau uses the **Ontario portion** of the CMA population.

## Scope and interpretation
The 15 CMAs do not represent all of Ontario, and caseload counts are not counts of distinct individuals served over a full year. OW and ODSP have different duration categories, so their duration breakdowns are displayed separately in combined-program mode. Associations and trends are descriptive, not causal estimates.

## Run locally
Serve the repository folder over HTTP, e.g. `python -m http.server 8000`, then open `http://localhost:8000/`. D3.js is loaded from jsDelivr, so an internet connection is needed for the library.

## Project assets
- `index.html`, `style.css`, `app.js`: dashboard
- `real_data.json`: processed dataset
- `ontario_15_cma_boundaries.geojson`, `ontario_context.geojson`, `ontario_full_boundary.geojson`: map geometry
- `scripts/build_data.py`: data preparation and validation

The course contribution report is a separate submission item and is not included here.
