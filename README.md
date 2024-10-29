# Basecamp Project

This project is a Django-based application that allows users to manage projects with features for collaboration and file sharing.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [The Core Team](#the-core-team)

## Features
- **Project Management**: Create and manage multiple projects.
- **Message Boards**: Each project has its own message board for user communication and updates.
- **File Uploads**: Upload images and files related to each project.
- **User Authentication**: Custom user model with email as the unique identifier.
- **Permissions and Roles**: Assign roles to team members (e.g., Team Lead, Team Member).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/junaidalam2/basecamp_part2_django
   cd basecamp```

2. **Clone the repository:**
```python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**
```python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. **Apply migrations:**
```python manage.py migrate```

5. **Create a superuser:**
```python manage.py createsuperuser```

6. **Run the development server:**
```python manage.py runserver```


## Configuration

In `settings.py`, configure the following:

- **ALLOWED_HOSTS**: Add your domain, e.g., `basecamp-part2-django.onrender.com`.
- **Static Files**: Set up static files in `STATIC_ROOT` and `STATICFILES_DIRS`.
- **Third-Party Authentication**: Set up Google and GitHub credentials in Django-Allauth settings.

## Usage

1. Access the application at `https://basecamp-part2-django.onrender.com`.
2. Log in with your account.
3. To login as an admin, use L: admin@gmail.com; P: password1
3. Explore project management, message boards, and file upload features.

## Directory Structure
.
├── src
│   ├── basecamp         # Main Django project
│   ├── projects         # Projects app
│   ├── users            # Custom user model and auth
│   ├── messages         # Message boards and messaging functionality
│   ├── staticfiles      # Directory for static files (CSS, JS, images)
│   └── templates        # HTML templates
└── README.md


### The Core Team

Junaid Alam

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt="Qwasar SV -- Software Engineering School's Logo" src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>

