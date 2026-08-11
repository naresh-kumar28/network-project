# Network Management System

Full-stack Network Management System built with Django, Django REST Framework, SimpleJWT, and React (Vite + Tailwind CSS).

---

## 📁 Repository Architecture

```text
network-project/
├── backend/                  # Django REST API Backend
│   ├── apps/
│   │   ├── accounts/         # Custom User, Auth, Tokens
│   │   ├── members/          # Member profiles & sponsor links
│   │   ├── plans/            # Membership plans
│   │   ├── epins/            # EPIN generation/validation
│   │   ├── network/          # Binary tree & referral tree logic
│   │   ├── income/           # Income calculations
│   │   ├── wallet/           # Wallet ledger
│   │   ├── withdrawals/      # Withdrawal management
│   │   ├── sales/            # Sales tracking
│   │   ├── kyc/              # KYC verification
│   │   └── notifications/    # Push / In-app notifications
│   ├── config/               # Project settings & URL routing
│   ├── .env.example          # Environment variables template
│   ├── manage.py
│   └── requirements.txt      # Python dependencies
├── docs/                     # Task assignments & architecture docs
└── frontend/                 # React Frontend
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd network-project
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows (PowerShell):
.\env\Scripts\Activate.ps1
# Linux / macOS:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp .env.example .env   # (or copy manually on Windows)

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Run Development Server
python manage.py runserver
```

Backend will start at: `http://127.0.0.1:8000/`

---

## 📚 API Documentation (Swagger)

Once the backend is running, access live interactive API docs at:
- **Swagger UI:** `http://127.0.0.1:8000/swagger/`

---

## 👥 Team Responsibilities & Workflow

- **Naresh (Backend Lead):** Core architecture, Custom User, Auth, Binary/Sponsor logic, Income Engine, Wallet calculation.
- **Prabhakar (Admin CRUD Backend):** Admin management endpoints, KYC verification APIs, Sales records, Notification endpoints.
- **Rahul (Frontend Lead):** React components, Tailwind styling, Dashboard UI, API integration with Axios.

### Git Branching Rules
- **DO NOT** push directly to `main`.
- Create feature branches:
  - `feature/auth-custom-user`
  - `feature/admin-crud-kyc`
  - `feature/frontend-dashboard`
- Submit Pull Requests (PRs) for review.
