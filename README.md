todo:
-favicon
-readme
-gmail/github configuration


# Basecamp Project

This project is a Django-based application that allows users to manage projects, message boards, and user authentication, including third-party logins with Google and GitHub.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Project Management**: Create and manage multiple projects with custom fields.
- **Message Boards**: Each project can have its own message board, allowing users to communicate and post updates.
- **File Uploads**: Users can upload images and files related to each project.
- **User Authentication**: Custom user model with email as the unique identifier.
- **OAuth Integration**: Google and GitHub login options are available.
- **Permissions and Roles**: Assign roles to team members (e.g., Team Lead, Team Member).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/basecamp.git
   cd basecamp


2. **Clone the repository:**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Apply migrations:**
python manage.py migrate

5. **Create a superuser:**
python manage.py createsuperuser

6. **Run the development server:**
python manage.py runserver


## Configuration

In `settings.py`, configure the following:

- **ALLOWED_HOSTS**: Add your domain, e.g., `basecamp-part2-django.onrender.com`.
- **Static Files**: Set up static files in `STATIC_ROOT` and `STATICFILES_DIRS`.
- **Third-Party Authentication**: Set up Google and GitHub credentials in Django-Allauth settings.

## Usage

1. Access the application at `http://127.0.0.1:8000`.
2. Log in with your superuser account.
3. Explore project management, message boards, and file upload features.
4. Enable Google or GitHub login for OAuth capabilities.


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


