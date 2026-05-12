# AGENTS.md

## Cursor Cloud specific instructions

This is a Django REST Framework backend for agricultural products ("webNongNghiep"). It has no frontend — the DRF browsable API serves as the UI.

### Services

| Service | Command | Port |
|---|---|---|
| Django dev server | `python3 manage.py runserver 0.0.0.0:8000` | 8000 |

SQLite is the database (file-based `db.sqlite3`); no external DB server is needed.

### Key commands

- **Run server:** `python3 manage.py runserver 0.0.0.0:8000`
- **Run tests:** `python3 manage.py test`
- **System check / lint:** `python3 manage.py check`
- **Migrations:** `python3 manage.py migrate`

### API endpoints

- `GET/POST /snippets/` — list/create code snippets
- `GET/PUT/DELETE /snippets/<id>/` — snippet detail
- `GET/POST /products/` — list/create products
- `GET/PUT/DELETE /products/<id>/` — product detail

### Gotchas

- The repo has **no `requirements.txt`**. Dependencies are: `django==3.1.4`, `djangorestframework`, `pygments`.
- Write endpoints require authentication (`DjangoModelPermissionsOrAnonReadOnly`). Read endpoints are public. Use `python3 manage.py createsuperuser` to create an account, then pass `-u user:pass` with curl or use session auth in the browsable API.
- There are no automated tests in the repo (0 test cases). `python3 manage.py test` runs but finds nothing.
- No linting tools (flake8, pylint, etc.) are configured in the repo; `python3 manage.py check` is the only built-in validation.
