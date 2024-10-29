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
```
bash
git clone https://github.com/junaidalam2/basecamp_part2_django
cd basecamp
```

2. **Clone the repository:**
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. **Apply migrations:** <br>
```
python manage.py migrate
```

5. **Create a superuser:** <br>
```
python manage.py createsuperuser
```

6. **Run the development server:** <br>
```
python manage.py runserver
```


## Configuration

In `settings.py`, configure the following:

- **ALLOWED_HOSTS**: Add your domain, e.g., `basecamp-part2-django.onrender.com`.
- **Static Files**: Set up static files in `STATIC_ROOT` and `STATICFILES_DIRS`.
- **Third-Party Authentication**: Set up Google and GitHub credentials in Django-Allauth settings.

## Usage

1. Access the application at <a href='https://basecamp-part2-django.onrender.com'>https://basecamp-part2-django.onrender.com</a>.
2. Log in with your account.
3. To login as an admin, use L: admin@gmail.com; P: password1
3. Explore project management, message boards, and file upload features.

## Directory Structure
.<br>
├── src<br>
│   ├── basecamp         # Main Django project<br>
│   ├── projects         # Projects app<br>
│   ├── users            # Custom user model and auth<br>
│   ├── messages         # Message boards and messaging functionality<br>
│   ├── staticfiles      # Directory for static files (CSS, JS, images)<br>
│   └── templates        # HTML templates<br>
└── README.md<br>


### The Core Team

Junaid Alam

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt="Qwasar SV -- Software Engineering School's Logo" src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>

