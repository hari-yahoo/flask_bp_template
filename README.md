# Flask Blueprint Template
This repository provides a Flask Blueprint template to help jump-start any Python project. It offers a clean and scalable structure to get started quickly with Flask web applications.

## Features
* Modular Structure: Blueprint-based modularity to separate and organize application components.
* Pre-configured Flask app: Ready-to-use Flask app setup with essential configurations.
* Scalable: Supports scaling with multiple Blueprints as the project grows.
* Minimal Dependencies: Keeps dependencies lightweight to ensure faster setup and flexibility.
* Template Rendering: Includes basic HTML templates using Jinja2 for easy front-end integration.
* Error Handling: Basic error handling is pre-configured.
* Session Management: Pre-configured session management for authentication purposes.
* SQLAlchemy Integration: Example setup for database integration with SQLAlchemy.
* Template for Static Files: Pre-configured structure for static files like CSS, JS, and images.
  
## Getting Started
This template is a starting point for Flask projects, designed to save you time on setup and help you focus on developing your application's core feature
### Prerequisites
Ensure you have the following installed:

- Python 3.8+
- pip for Python package management
- Virtual Environment (recommended)

## Installation
1. Clone the repository
  ```
  git clone https://github.com/hari-yahoo/flask_bp_template.git
   
  cd flask-blueprint-template 
  ```
1. Setup virtual environment
```
python3 -m venv venv
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
```
   
2. Install dependencies
```
pip install -r requirements.txt
```
6. Run flask application
```
flask run
```

## Project Structure
```
.
├── app/
│   ├── __init__.py          # Initialize Flask app and register Blueprints
│   ├── main/
│   │   ├── __init__.py      # Main Blueprint setup
│   │   ├── routes.py        # Main routes for the application
│   │   └── templates/       # HTML templates
│   └── static/              # Static files (CSS, JS, Images)
├── config.py                # Configuration settings for Flask app
├── requirements.txt         # Python dependencies
├── app.py                   # Entry point to run the Flask app
└── README.md                # Project documentation

```
## Usage
### Blueprints: 
Use the provided main Blueprint as an example to create additional Blueprints and modularize the application.
### Templates and Static Files: 
Add or modify HTML templates and static files under their respective directories.
### Database: 
Modify the SQLAlchemy configuration in config.py for database usage.
### Contributing
Feel free to contribute by submitting pull requests or opening issues. Your contributions are greatly appreciated!