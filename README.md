# The Changing Face of Social Assistance

## Team preview
Interactive D3.js dashboard using processed Ontario OW/ODSP and Statistics Canada CMA data.

## Run locally
Open the entire folder in VS Code and use Live Server on `index.html`. Opening `file://` directly will not reliably load JSON/GeoJSON due to browser security restrictions.

## Publish with GitHub Pages
1. Create a new public GitHub repository for the team preview, or use a separate branch/folder in an existing repository.
2. Upload the **contents** of this folder to the repository root (not the enclosing folder).
3. In repository **Settings → Pages**, select **Deploy from a branch**, branch `main`, folder `/(root)`, then Save.
4. Wait for the published site URL in Settings → Pages. Open it in an incognito window and test controls.
5. Share the URL with group members.

## Data
- `real_data.json`: processed annual CMA rates and characteristics used by the dashboard.
- `ontario_15_cma_boundaries.geojson`: simplified Statistics Canada 2021 CMA cartographic boundaries.
- `ontario_context.geojson`: Ontario/Quebec shoreline context derived from Statistics Canada 2021 provincial cartographic boundaries.

## Before final course submission
This is a team-review / deployment-ready package, not yet a complete reproducibility archive. Add raw input datasets, executable data-preparation scripts, source links and a calculation audit; confirm the final submission rubric. D3.js is loaded from jsDelivr, so internet is needed.

## Development plan
See `DEVELOPMENT_PLAN.txt`. Member responsibilities are proposed and should be confirmed with the team.
