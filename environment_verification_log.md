# Prompt 08 — Environment verification log

**Project folder:** `AITR_Lab02_MHM2026001_ContextWindowDegradation`  
**Date:** 2026-10-30  

## Commands run

```bash
cd AITR_Lab02_MHM2026001_ContextWindowDegradation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/env_test.py
python scripts/unit_smoke.py
```

## Actual outcome (recorded)

- `python`: 3.14.x on macOS arm64 (M2 host)  
- Imports: PyYAML OK, requests OK, python-dotenv OK  
- Packets load; begin/middle/end assembly prints orders  
- `scripts/env_test.py` → **STATUS: PASS**  
- `scripts/unit_smoke.py` → **PASS**  

## Failure diagnostics (if env_test fails)

- Missing deps → reinstall `requirements.txt`  
- No packets → check `data/packets/item_*.json`  
- Import errors → ensure `src/` is on `PYTHONPATH` via scripts’ path insert  

## Human note

Dummy backend inside env_test is only a wiring check. Scientific baseline uses Groq via `.env`.
