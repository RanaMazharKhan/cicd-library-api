# Library API (CI/CD learning project)

A tiny Django project we're building step by step to learn how a
CI/CD pipeline works.

## How to run it on your computer

1. Open this folder in VS Code.
2. (Recommended) create a virtual environment so packages don't mix
   with other projects:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```
3. Install the one thing we need so far:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database (just creates an empty db.sqlite3 file for now):
   ```
   python manage.py migrate
   ```
5. Start the server:
   ```
   python manage.py runserver
   ```
6. Open your browser to:
   - http://127.0.0.1:8000/        → should say "Welcome to my Library API!"
   - http://127.0.0.1:8000/health/ → should say {"status": "ok"}

If you see those two messages, it's working! If you see an error
instead, copy the error text and we'll fix it together.

## What's next

This is just Step 1 (the app itself). Next we'll add automatic
tests, then a Dockerfile, then a GitHub Actions pipeline that runs
everything automatically.
