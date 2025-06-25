# Inovex

## Overview
Inovex is a modular, containerized software platform designed to empower startups and enterprises with scalable, cloud-native digital solutions. The project features a microservices-based backend and a multi-page frontend, supporting admin and user dashboards, and is built for rapid digital transformation.

## Features
- Microservices architecture (Flask-based Python services)
- Modular frontend (HTML, CSS, JS)
- Admin and user dashboards
- Container-ready (Dockerfiles for each service)
- Scalable and easy to deploy

## Folder Structure
```
InnovexApplication-main/
  backend/
    admin-service/
    auth-service/
    careers-service/
    contact-service/
  frontend/
    aboutus-frontend/
    admin-frontend/
    auth-frontend/
    careers-frontend/
    contact-frontend/
    home-frontend/
    industries-frontend/
    services-frontend/
```

## Getting Started
1. **Clone the repository:**
   ```sh
   git clone https://github.com/AnjanKumarS/Inovex.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd InnovexApplication-main
   ```
3. **Set up Python virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```
4. **Install backend dependencies:**
   ```sh
   pip install -r backend/admin-service/requirements.txt
   pip install -r backend/auth-service/requirements.txt
   pip install -r backend/careers-service/requirements.txt
   pip install -r backend/contact-service/requirements.txt
   ```
5. **Run backend services:**
   ```sh
   python backend/admin-service/app.py
   python backend/auth-service/app.py
   python backend/careers-service/app.py
   python backend/contact-service/app.py
   ```
6. **Open frontend HTML files in your browser** (e.g., `frontend/home-frontend/index.html`).

## Docker Support
Each service and frontend has its own Dockerfile for containerized deployment.

## Team
- Anjan Kumar S (CEO & Founder)
- Roshan Ameen (Chief Technology Officer)
- Rahul Dev (Technical Advisor)

## License
&copy; 2025 Inovexa. All rights reserved.