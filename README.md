# Registration Project

A Django-based user registration system with Excel export functionality.

## Features

- User registration with form validation
- Success messages
- Excel export of registered user data
- Responsive design

## Setup Instructions

1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the server: `python manage.py runserver`

## Technologies Used

- Django
- SQLite
- HTML/CSS
- openpyxl (for Excel export)

## Project Structure

- `register_app/` - Main application with registration functionality
  - `models.py` - Database models
  - `forms.py` - Form handling and validation
  - `views.py` - View logic for registration and data export
  - `templates/` - HTML templates
