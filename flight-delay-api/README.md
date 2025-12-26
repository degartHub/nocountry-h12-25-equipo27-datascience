# Flight Delay API

## Run locally

```bash
cd flight-delay-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.app:app --reload