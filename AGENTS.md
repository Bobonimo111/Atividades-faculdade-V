# AGENTS.md — Coisas-de-Kaio

Multi-project academic portfolio (student assignments). Each subdirectory is an independent project.

## Project map

| Directory | Language | Pattern/Topic | Entrypoint |
|---|---|---|---|
| `atividade-designe-software/` | Java (plain, no build tool) | Factory pattern — notification (SMS/Email) | `src/Main.java` |
| `exemploStrategy-designe-software/` | Java (plain, no build tool) | Strategy pattern — file save (Image/PDF) | `src/Main.java` |
| `atividade-fim-semestre-ia-kaio/` | Python (Jupyter + Streamlit) | Bank Marketing classification (Kaggle) | `analise.ipynb`, `streamlit_app.py` |
| `atv-meio-semestre-kaio-analise-de-dados/` | Python (Jupyter) | Student performance regression (Kaggle) | `at.ipynb` |
| `Segunda AT Ia/` | Python (script) | Mode calculation | `moda.py` |

## Commands

- **Python notebooks**: open in VS Code/Jupyter and run cells
- **Streamlit app** (`atividade-fim-semestre-ia-kaio/`): `streamlit run streamlit_app.py` (uses `.venv`)
- **Python scripts**: `py -3 Segunda AT Ia/moda.py` (standalone, stdlib only)
- **Java projects**: open in IntelliJ IDEA and run `Main.java` (no Maven/Gradle — plain IntelliJ modules)
- **No tests, no linters, no CI** in any project

## Gotchas

- **Hardcoded API key** — `analise.ipynb` exposes a Google Gemini API key as a plaintext string. Do not commit. Use env vars.
- Data for the Bank Marketing notebook is downloaded by `kagglehub` (first cell) into `data-set/`.
- `Segunda AT Ia/moda.py` reads inline data (list literal), not `NumberMap.json`.

## Conventions

- Java: `out/` is IntelliJ build output dir; both `atividade-designe-software/` and `exemploStrategy-designe-software/` are plain IntelliJ modules (no build tool)
- Python: `.venv/` in each project dir has its own `*.gitignore` — its content is gitignored via venv's built-in ignore rule
- All commits are direct pushes to `main` — no PR workflow
- `NumberMap.json` at root is a standalone frequency map (unused by any project)
