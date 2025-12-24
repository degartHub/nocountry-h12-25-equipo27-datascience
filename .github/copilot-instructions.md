# Copilot instructions for this repository

Purpose
- Help AI coding agents become productive quickly in this Data Science repo.

**Big Picture (how this repo is organized and why)**
- Data ingestion: `data/` contains CSVs (e.g. `Airline_Delay_Cause.csv`, `Airlines.csv`) and a column-translation file `Siglas_columnas_aeropuertos`.
- Analysis & orchestration: canonical pipelines and exploratory work live in notebooks such as `H12_25_L_Equipo_27_Data_Science.ipynb` and `main_pipeline.ipynb`.
- Reusable code: `src/` contains helper functions and modularized code that notebooks import. Prefer adding new reusable functions here rather than embedding large logic directly in notebooks.
- Models: trained artifacts are stored under `models/` (typically as `joblib` or similar).
- Tests: `tests/` contains unit tests for `src` modules; keep logic in `src` small and easily testable.

**Developer workflows and commands**
- Setup virtualenv and install deps: `python -m venv .venv` then `pip install -r requirements.txt`.
- Run unit tests: `pytest tests/` (add pytest to `requirements.txt` if missing).
- Open notebooks locally: launch Jupyter (`jupyter lab` or `jupyter notebook`) and run `main_pipeline.ipynb` for the canonical pipeline.
- When adding or changing model training code, ensure the produced artifact is saved to `models/` and referenced by notebooks/tests via relative paths.

**Project-specific conventions and patterns**
- Notebook-first development: experiments and EDA belong in `/notebooks` and the two top-level notebooks. When a pattern stabilizes, extract to `src/` and add tests.
- Small, focused modules: `src` modules should expose functions (not top-level scripts) so `pytest` can import and run them.
- Data immutability: do not modify files in `data/` in-place. If transformations are needed, write derived files to `data/derived/` or `models/`.
- Model persistence: use `joblib.dump` / `joblib.load` (or equivalent) and store paths under `models/` with clear names.

**Integration points & external assumptions**
- Notebooks are often run in Google Colab; keep cells that depend on local filesystem guarded or provide an alternative for Colab (e.g., mount drive or download dataset).
- There are no configured CI/CD files in the repo; assume manual `pytest` checks locally unless CI is added.

**Examples & concrete pointers**
- To find the main pipeline, open `main_pipeline.ipynb` — it shows the expected sequence: load `data/` → feature engineering (extracted into `src/` as project matures) → train → save to `models/`.
- Reusable helpers should live in `src/` and be imported in notebooks like `from src.preprocessing import clean_dates`.
- Reference dataset names exactly: `data/Airline_Delay_Cause.csv` etc., to avoid breaking notebook paths.

**What AI agents should do (practical rules)**
- Prefer adding tests in `tests/` for any new `src/` functionality.
- When modifying notebooks, also update or add a small `.py` wrapper under `src/` and include a unit test.
- Avoid changing raw data files or renaming dataset files without updating all notebooks that reference them.
- If a dependency is required, add it to `requirements.txt` and include a one-line note in the same commit message.

If anything here is unclear or you'd like a different focus (e.g., more CI instructions, linter rules, or example PR templates), tell me which section to expand.
