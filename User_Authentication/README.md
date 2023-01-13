#### About
User Authentication project in Django

![Alt Text](user_auth.png)
#### Steps.

1. Run the following command to activate virtualenv
```
virtualenv env
source ./env/bin/activate
```
2. 
Install django inside the virtual env
```
pip install django
```
3. create a project authentication_portal 
```
django-admin startproject authentication_portal
```
4. create an app named authenticator inside it
```
cd authentication_portal
django-admin startapp authenticator
```
5. Modify authenticator in INSTALLED_APPS of settings.py
6. Create urls.py in authenticator app besides the project level urls.py
7. Ensure modification in urls.py is there at project and app level, both. Make sure to derive Django authentication system url in project level urls. It'll save time in building an authentication portal from scratch.
8. To create the authentication page's html page and css - create templates, static/css and static/images directory in the authentictor app directory.
9. Create base.html and paste sample bootstrap code in it and then create authenticator.html
10. Create a view in views.py to render the html page in the authenticator app directory.
11. Create a bootstrap form and put in authenticator.html
12. Check the page by visiting - http://127.0.0.1:8000 after executing
```
python manage.py runserver
```
13. Convert django models into tables via makemigrations and migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
username - user
password - password@123
