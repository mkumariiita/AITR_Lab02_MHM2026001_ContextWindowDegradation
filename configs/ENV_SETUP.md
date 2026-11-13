# `.env` setup (not a folder)

Use a **file** named `.env` in the project root:

`AITR_Lab02_MHM2026001_ContextWindowDegradation/.env`

## What to add

| Variable | Required? | Example |
|---|---|---|
| `LLM_API_KEY` | yes (for real runs) | `gsk_...` from Groq |
| `LLM_BASE_URL` | yes | `https://api.groq.com/openai/v1` |
| `LLM_MODEL` | yes | `openai/gpt-oss-20b` |
| `LLM_BACKEND` | optional | `openai_compat` |

## Steps

```bash
cd AITR_Lab02_MHM2026001_ContextWindowDegradation
cp .env.example .env
# edit .env — paste your key (only on your machine)
```

Then:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_baseline.py --backend openai_compat --limit 2
```

## Safety

- `.env` is in `.gitignore` — do not force-add it to git
- Do not paste the key into Cursor chat
- `.env.example` is safe to share (placeholders only)