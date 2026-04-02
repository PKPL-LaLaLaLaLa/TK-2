# TK-2 PKPL — Biodata App

## Setup

```bash
# 1. Buat virtual environment
python -m venv env

# 2. Aktifkan virtual environment
env\Scripts\activate        # Windows
source env/bin/activate     # Mac / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Buat file .env (salin dari template, lalu isi credentials kamu)
copy .env.example .env      # Windows
cp .env.example .env        # Mac / Linux

# 5. Migrate database
python manage.py migrate
```

## Run

```bash
env\Scripts\activate
python manage.py runserver
```

Buka: **http://localhost:8000**
