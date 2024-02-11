# Matching Platform Project

This repository contains the Django-based Matching Platform project, designed for matching users with projects based on their interests and requirements. It leverages Django's robust framework to create a dynamic and interactive platform where users can find projects tailored to their preferences, powered by both traditional web development practices and ML technique. 

NOTE: It utilizes a Content-Based Filtering approach, leveraging TF-IDF and cosine similarity to generate recommendations as a starting point. This is an ongoing process.

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