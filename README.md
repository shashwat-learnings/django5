# Django Project Setup and Server Commands

## 1. Activate Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```
*Creates and activates a virtual environment named `venv`.*

## 2. Create a New Django Project

If not created the folder

```
pip install django
django-admin startproject <project_name>
```
else

```
pip install django
django-admin startproject <project_name> .
```

*Installs Django and creates a new project. Replace `<project_name>` with your desired project name.*

## 3. Create a New Django App
```
python manage.py startapp app1
```

## 4. Run Server for a Different Project

Navigate to the project directory and run:
```
cd <project_name>
python manage.py runserver
```
*Starts the Django development server for the specified project.*
*To start the server on another port other than 8000 just put port number next to runserver .e.g. python manage.py runserver 4000*



## 5. If venv is not auto selecting

hit cmd+shift+p and search python interpeter  



