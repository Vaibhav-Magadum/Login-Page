# Login-Page

A simple login page built with Python and Flask.

## Features

- User login with username and password
- User registration with password confirmation
- Session-based authentication
- Flash messages for user feedback
- Responsive design

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   python app.py
   ```

3. **Open your browser** and go to `http://127.0.0.1:5000`

## Default Credentials

- **Username:** `admin`
- **Password:** `admin123`

## Project Structure

```
Login-Page/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # CSS styles
├── templates/
│   ├── login.html         # Login page template
│   ├── register.html      # Registration page template
│   └── dashboard.html     # Dashboard page template
└── README.md
```