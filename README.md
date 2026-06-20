# Library API — CI/CD Pipeline Testing Project

A small Django web API, built step by step to learn and demonstrate how a
**CI/CD pipeline** works in real software development — created for a
Software Quality Engineering exam project.

The goal isn't the app itself (it's intentionally simple) — it's showing
every stage a real engineering team relies on to ship code safely:
writing it, testing it automatically, checking its code quality, packaging
it, and (next) deploying it through an automated pipeline.

## Tech stack

- **Python / Django** — the application itself
- **Django's test framework** — automated unit tests
- **flake8** — static code analysis / linting
- **Docker** — containerization, so the app runs identically anywhere
- **GitHub Actions** — automated CI/CD pipeline *(in progress)*

## Project structure

```
cicd-project/
├── config/             # Project-wide settings and URL routing
├── library/            # The app itself
│   ├── views.py        # Request handlers
│   ├── urls.py         # App-level routes
│   └── tests.py        # Automated tests
├── Dockerfile           # Container build instructions
├── .dockerignore
├── .flake8              # Linting rules
├── requirements.txt      # Runtime dependencies
├── requirements-dev.txt  # Dev-only tools (linting, etc.)
└── manage.py
```

## What's implemented so far

- [x] Django app with a homepage and a `/health/` check endpoint
- [x] Automated tests covering both endpoints
- [x] Static code analysis with flake8 as a quality gate
- [x] Fully containerized with Docker
- [ ] Automated CI/CD pipeline via GitHub Actions — **next step**
- [ ] Deployment stage

## Running it locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/health/`.

## Running with Docker

```bash
docker build -t library-api .
docker run -p 8000:8000 library-api
```

## Running the tests

```bash
python manage.py test
```

## Running the linter

```bash
python -m flake8 .
```

## Roadmap

1. ~~Build the app~~
2. ~~Add automated tests~~
3. ~~Add static analysis (flake8)~~
4. ~~Containerize with Docker~~
5. Automate all of the above with a GitHub Actions pipeline
6. (Optional) Add security scanning and a deployment stage
