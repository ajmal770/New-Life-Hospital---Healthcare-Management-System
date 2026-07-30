# 🏥 New Life Multispecialty Hospital Management System

> **Tagline:** *Healing Lives, Building Hope.*

A world-class, full-stack Hospital Management Web Application built with Python (Flask), SQLite (SQLAlchemy), and modern UI/UX principles inspired by global healthcare leaders like Apollo Hospitals, Mayo Clinic, and Cleveland Clinic.

---

## 🌟 Repository Overview & Short Description

**GitHub About Description:**
```text
🏥 New Life Multispecialty Hospital — World-class enterprise healthcare portal featuring doctor scheduling, real-time appointment booking, double-booking prevention, department catalogs, and glassmorphism UI. Built with Flask, SQLAlchemy, & Bootstrap 5.
```

---

## ✨ Key Features

- **🏆 Apollo & Mayo Clinic Inspired Hero Section**: Full-screen responsive hero header with dynamic typography, floating glassmorphism appointment & emergency cards, trust badges, and hospital statistics counter.
- **⚡ Real-Time Appointment Booking**: Conflict-free online appointment booking system with automated time slot generation.
- **🛡️ Double-Booking Prevention Logic**: Backend SQLAlchemy query checks to prevent scheduling two appointments for the same doctor at the same date and time slot.
- **🩺 Specialist Directory & Schedules**: Comprehensive doctor directory with individual schedule tracking and department badges.
- **🏢 Specialized Departments Catalog**: Detailed showcase of Centers of Excellence (Cardiology, Neurology, Pediatrics, Orthopedics, Dermatology, Laboratory Services).
- **🎨 Glassmorphism & Modern UI Design**: Glassmorphic card overlays, custom HSL color tokens, dark mode footers, responsive typography, and micro-interactions.
- **📞 24/7 Helpline & Emergency Badge**: Integrated instant helpline badge (`1800-233-4567`) across navbar and footer.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask Web Framework
- **Database**: SQLite, Flask-SQLAlchemy (ORM)
- **Security**: Flask-WTF (CSRF Protection), Form Validation
- **Frontend**: HTML5, Vanilla CSS3, Bootstrap 5.3, Bootstrap Icons, Google Fonts (Poppins & Inter)
- **Templating**: Jinja2 Engine

---

## 📂 Project Structure

```text
Hospital Management/
├── app/
│   ├── __init__.py            # Flask App initialization & DB setup
│   ├── models.py              # SQLAlchemy Data Models (Doctor, Appointment)
│   ├── routes.py              # Application Controllers & Route Handlers
│   ├── forms.py               # Flask-WTF Forms & Validation Rules
│   ├── utils.py               # Helper Functions (Time slot generator)
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Custom Enterprise Design System
│   │   ├── js/
│   │   │   └── app.js         # Client-side Interactive Scripts
│   │   └── img/               # Department & Facility Images
│   └── templates/
│       ├── base.html          # Base Layout & Google Fonts Integration
│       ├── navbar.html        # Navigation Bar & Brand Emblem
│       ├── footer.html        # Rebuilt Enterprise Dark Footer
│       ├── home.html          # Main Landing Page & Hero Section
│       ├── booking.html       # Appointment Booking Form & List
│       ├── doctors.html       # Doctors Directory Page
│       ├── departments.html   # Departments Showcase Page
│       └── doctor_schedule.html # Individual Doctor Schedule Page
├── run.py                     # Entry point server script
├── requirements.txt           # Python Project Dependencies
└── README.md                  # Project Documentation
```

---

## ⚡ Quick Start Guide

### Prerequisites
- Python 3.8+ installed on your system.

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/new-life-hospital.git
   cd new-life-hospital
   ```

2. **Create & Activate a Virtual Environment**
   - **Windows:**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python run.py
   ```

5. **Open in Browser**
   Navigate to `http://127.0.0.1:5000/` in your web browser.

---

## 🌐 Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Main Home Landing Page |
| `/booking` | `GET`, `POST` | Patient Appointment Booking & Conflict Check |
| `/doctors` | `GET` | Medical Specialists Directory |
| `/doctor/<id>` | `GET` | Individual Doctor's Schedule & Appointments |
| `/departments` | `GET` | Specialized Medical Departments |

---

## 📄 License & Attribution

Designed and developed for **New Life Multispecialty Hospital** — *Healing Lives, Building Hope.*
