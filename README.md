# Matching Platform Project

This repository contains the Django-based Matching Platform project, designed for matching users with projects based on their interests and requirements. Below is the detailed structure and components of the project.

## Project Structure

The project is organized into several key directories and files:

### Core Django Application (`core/`)
- `__init__.py`: Initialization file for the core app as a Python package.
- `migrations/`: Contains database migration files.
- `admin.py`: Admin site configuration for the Django admin interface.
- `apps.py`: Core app configuration.
- `forms.py`: Forms used for user input.
- `models.py`: Defines Django models for UserProfile and Project.
- `views.py`: View functions to handle HTTP requests and responses.
- `serializers.py`: Serializers for converting model instances to JSON format.
- `tests.py`: Contains test cases for the core app.
- `urls.py`: URL declarations for the core app's views.

### Main Django Project (`matchmaking_platform/`)
- `__init__.py`: Initialization file for the project as a Python package.
- `asgi.py`: Entry-point for ASGI-compatible web servers.
- `settings.py`: Configuration settings for the Django project.
- `urls.py`: Main URL declarations for the entire project.
- `wsgi.py`: Entry-point for WSGI-compatible web servers.

### Templates (`templates/`)
- `home.html`: Template for the home page.
- `dashboard.html`: Template for the user dashboard.
- `profile.html`: Template for the user profile page.
- `projects.html`: Template for the projects listing page.
- `register.html`: Template for user registration.
- `login.html`: Template for user login.

### Media Files (`media/`)
- Directory for storing user-uploaded media files like images.

### Static Files (`static/`)
- `css/style.css`: Main stylesheet for the project's front-end design.
- `js/script.js`: JavaScript file for front-end interactivity.

### Root Directory
- `manage.py`: A command-line utility for Django administrative tasks.

## Getting Started

To get started with the Matching Platform project, follow these steps:

1. **Clone the Repository**
   ```
   git clone [repository-url]
   cd matching_platform
   ```

2. **Set Up a Virtual Environment (Optional but recommended)**
   ```
   python3 -m venv [your_venv_name]
   source [your_venv_name]/bin/activate 
   ```

3. **Run Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Development Server**
   ```
   python manage.py runserver
   ```

Now, visit http://localhost:8000 in your browser.