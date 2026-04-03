# LaLaLaLaLa — TK-2 PKPL

A modernized profile and biodata application built with Django.

## How to Run

Follow these steps to set up the project locally:

### 1. Init & Activate Virtual Environment
Create a virtual environment to manage dependencies:
```bash
# Init
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (Mac/Linux)
source env/bin/activate
```

### 2. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Copy the template file and fill in your credentials (do not commit your actual `.env` file):
```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```
Inside the `.env` file, ensure you have your Google OAuth credentials:
```env
GOOGLE_CLIENT_ID=your-google-client-id-here
GOOGLE_CLIENT_SECRET=your-google-client-secret-here
```

### 4. Migration
Prepare and apply the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seeding
Populate the database with initial member data:
```bash
python seed_data.py
```

### 6. Run Server
Launch the development server:
```bash
python manage.py runserver
```
Once running, you can access the application at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---
Built with ❤️ by Team LaLaLaLaLa
