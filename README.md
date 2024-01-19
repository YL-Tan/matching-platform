# Matching Platform Project

This repository contains the Django-based Matching Platform project. It's structured as follows:

## Project Structure

Below is the directory structure and a brief description of each component in the project:

### Core Django Application
- `core/`: The main Django app for core functionality.
  - `__init__.py`: Initialization file for the Python package.
  - `migrations/`: Directory for database migrations.
  - `admin.py`: Configuration for the Django admin interface.
  - `apps.py`: App-specific configuration.
  - `models.py`: Django models for UserProfile and Project.
  - `views.py`: Views for handling REST API requests.
  - `serializers.py`: Serializers for converting models to JSON format.
  - `urls.py`: URL declarations for the core app.
  - `tests.py`: Test cases for the app.

### Main Django Project
- `matchmaking_platform/`: The main Django project folder.
  - `__init__.py`: Initialization file for the Python package.
  - `asgi.py`: ASGI configuration for running the project.
  - `settings.py`: Django settings, including database configuration.
  - `urls.py`: Main URL declarations for the project.
  - `wsgi.py`: WSGI configuration for running the project.

### Templates
- `templates/`: Directory for HTML templates.
  - `index.html`: The main HTML structure for the front-end.

### Static Files
- `static/`: Directory for static files like CSS and JavaScript.
  - `css/`: Contains CSS files.
    - `style.css`: Main stylesheet for the project.
  - `js/`: Contains JavaScript files.
    - `script.js`: JavaScript for dynamic front-end functionality.

### Other Files
- `manage.py`: Django's command-line utility for administrative tasks.

## Getting Started

instructions on how to set up and run the project

## License
