# Flask + MySQL CRUD — README

A minimal, production-ready starter for a Flask CRUD app backed by MySQL. It includes a simple `User` model, Bootstrap-based pages (List/Add/Edit), and clear setup steps for Windows/macOS/Linux.

---

## 🚀 Features

- Flask + SQLAlchemy ORM
- MySQL database (with `PyMySQL` driver recommended)
- Bootstrap 5 UI (responsive table, forms, buttons)
- CRUD: Create, Read, Update, Delete Users
- Simple, extensible structure

---

## 📦 Tech Stack

- **Python**: 3.10+ (tested with 3.11/3.12/3.13)
- **Flask**: Web framework
- **Flask SQLAlchemy**: ORM
- **MySQL**: Database
- **PyMySQL**: DB driver (Windows friendly)
- **Bootstrap 5**: Frontend styling

---

## ✅ Prerequisites

- Python installed and on PATH
- MySQL Server running locally (or a remote MySQL instance)
- A database created for this app (e.g., `flaskdb`)

> **Tip:** Keep DB credentials out of source code. Use environment variables or a `.env` file.

---

## 🗂️ Project Structure

```
flask_crud_mysql/
├─ app.py
├─ requirements.txt
└─ templates/
   ├─ index.html
   ├─ add.html
   └─ edit.html
```

---

## 🔧 Setup & Run

### 1) Clone / Copy project

```bash
# inside your workspace directory
cd flask_crud_mysql
```

### 2) Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, install directly:

```bash
pip install flask flask-sqlalchemy pymysql
```

### 4) Create MySQL database

Log in to MySQL and create the DB:

```sql
CREATE DATABASE flaskdb;
```

### 5) Configure database URL

Set your SQLAlchemy URI via environment variable (recommended):

```bash
# Windows (PowerShell)
$env:SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<USER>:<PASSWORD>@localhost/flaskdb"

# macOS/Linux (bash/zsh)
export SQLALCHEMY_DATABASE_URI="mysql+pymysql://<USER>:<PASSWORD>@localhost/flaskdb"
```

Or hardcode in `app.py` (not recommended for prod):

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<USER>:<PASSWORD>@localhost/flaskdb'
```

> Replace `<USER>` and `<PASSWORD>` with your actual MySQL credentials.

### 6) Initialize tables & run the app

```bash
python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Endpoints (UI)

- `GET /` — List users
- `GET|POST /add` — Create user
- `GET|POST /edit/<id>` — Update user
- `GET /delete/<id>` — Delete user (with confirm in UI)

> You can later add JSON APIs (e.g., `/api/users`) if you want to connect React/Angular.

---

## 🧰 Example `requirements.txt`

```txt
flask>=3.0
flask-sqlalchemy>=3.1
pymysql>=1.1
# Optional: python-dotenv if you choose to load env vars from .env
python-dotenv>=1.0
```

---

## 🎨 Frontend (Bootstrap 5)

This project uses Bootstrap via CDN in the templates. Ensure your templates include:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

---

## 🔒 Environment Variables (optional but recommended)

Create a `.env` file (and load it in `app.py` using `python-dotenv`) to keep secrets out of code.

**.env**

```dotenv
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<USER>:<PASSWORD>@localhost/flaskdb
FLASK_ENV=development
FLASK_DEBUG=1
```

Load in `app.py`:

```python
from dotenv import load_dotenv
import os
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
```

---

## 🧯 Troubleshooting

### 1) `Access denied for user 'root'@'localhost' (using password: YES)`

- Verify credentials are correct
- Confirm you can log in: `mysql -u <USER> -p`
- If using Windows, prefer `PyMySQL` driver in the URI: `mysql+pymysql://...`
- Ensure DB exists: `CREATE DATABASE flaskdb;`

### 2) Driver/connector errors on Windows

- Install `pymysql`: `pip install pymysql`
- Use `mysql+pymysql://...` in the URI

### 3) Cannot import package / venv issues

- Confirm venv activated (see prompt has `(.venv)`)
- Reinstall deps: `pip install -r requirements.txt`

### 4) Port already in use

- Stop other apps on `5000`, or run: `python app.py --port 5001`

---

## 🧩 Extending the App

- Add pagination, search, and sort to the Users table
- Add server-side validation and unique constraints (e.g., unique email)
- Implement JSON REST API
- Add authentication (Flask-Login / JWT)
- Use Alembic for DB migrations

---

## 📝 License

MIT (or your preferred license)

---

## 🙌 Credits

Built with ❤️ using Flask, SQLAlchemy, Bootstrap, and MySQL.

