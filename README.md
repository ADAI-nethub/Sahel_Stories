
<img width="955" height="611" alt="image" src="https://github.com/user-attachments/assets/30fd5bc2-2a43-4233-affd-c348394e65a8" />
# Sahel Stories 

*A Django web application that connects cultural storytelling in the Sahel region with real tree planting.*

Each time a visitor listens to a story from a local artisan, a symbolic (or future real) tree is planted — turning empathy into environmental action.

Built as a beginner-friendly, ethical tech project aligned with the **Great Green Wall Initiative**.

![Render Dashboard - Sahel_Stories-1](https://github.com/user-attachments/assets/6fc772c6-2b00-49c4-85bc-ef391d235c2b)

---

## Live Demo

✅ **Deployed on Render**:  
 [https://sahel-stories-1.onrender.com](https://sahel-stories-1.onrender.com)

 **Admin Panel**:  
[https://sahel-stories-1.onrender.com/admin](https://sahel-stories-1.onrender.com/admin)

 **Service ID**: `srv-d2u86undiees73cmmmf0`  
 **Hosted on**: [Render.com](https://render.com)  
 **Repository**: [ADAI-nethub / Sahel_Stories](https://github.com/ADAI-nethub/Sahel_Stories)

---

## 🛠 What I’ve Achieved So Far

After overcoming multiple deployment challenges, here is what has been successfully completed:

### ✅ Fixed Critical Deployment Errors
- Resolved Git merge conflicts in `settings.py` and `urls.py`
- Removed system packages (`Brlapi`, `apturl`) from `requirements.txt`
- Regenerated a clean, production-ready `requirements.txt`

### ✅ Configured Environment Variables
- Set `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS`
- Ensured secure and stable production settings

### ✅ Connected to PostgreSQL
- Created a PostgreSQL instance on Render
- Linked it via `DATABASE_URL`
- Successfully ran `python manage.py migrate`

### ✅ Admin & Authentication
- Created a superuser via **Render Shell**
- Verified login to Django Admin is working

### ✅ Static Files Served via Whitenoise
- CSS, JS, and images now load correctly in production

### ✅ Google Sheets Integration (Prepared)
- Code ready to sync tree planting data using `gspread`
- Secure credential loading via environment variables

---

## 🎯 Executive Summary

**Sahel Stories** is a Django web application that centers local voices from the Sahel region by digitizing oral stories about drought, trees, traditions, and survival — and linking each "listen" to a symbolic tree planting.

![Project Poster](https://github.com/user-attachments/assets/5b7bc2ec-722d-4071-ab17-49a18d692c13)

### Built with:
> Artisan stories (text/audio)  
>  "Listen & Plant" action  
>  Tree planting tracker  
>  Django Admin for content management  
>  Designed for future SMS/WhatsApp access  
>  Not a full tourism platform — just a focused, ethical step toward one.

---

## Features

- Artisan profiles (local storytellers)
- Story listings with location and transcript
- “Listen & Plant” action (simulated tree planting)
- Tree planting tracker (with visitor name & date)
- Admin interface for managing content
- Simple HTML frontend (Django templates)
- Responsive design with Bootstrap
- Map view using GeoJSON (in progress)

---

## Core Purpose

This web app supports **cultural preservation** and **climate action** by allowing:

- 🧑‍🌾 **Artisans** to share stories of resilience and tradition  
- 👂 **Visitors** to listen and trigger a symbolic tree planting  
- 🛠 **NGOs** to manage content via Django Admin  
- 🌍 **The planet** to benefit from verified reforestation (future phase)

> 💬 *"We believe that stories are seeds. When shared with care, they can grow forests, revive traditions, and connect people across continents."*

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, Django Templates |
| API | Django REST Framework |
| Database | SQLite (local), PostgreSQL (production) |
| Hosting | Render.com |
| Version Control | GitHub |
| Environment | Python 3.10+, Virtual Environment |
| Deployment | Gunicorn, Whitenoise, `requirements.txt` |

---

## Impact

- ✅ Preserves oral traditions of the Sahel
- ✅ Logs every "tree planted" action
- ✅ Designed for future integration with SMS/WhatsApp (Twilio)
- ✅ Beginner-accessible codebase with clear comments
- ✅ Ethical by design — no gamification, no exploitation

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/ADAI-nethub/Sahel_Stories.git
cd Sahel_Stories

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver

# 7. Visit
http://127.0.0.1:8000
