# Creating a Django project and deploying it on Heroku.
#### Steps
1. Open VSCode and create a virtual env named env using 
``` 
$ virtualenv env
```
2. Activate the created env by going inside the env folder visible from explorer view by running 
```
$ sudo chmod -R 777 env/
$ source ./env/bin/activate
```
3. Check all the packages in the project via pip freeze and install django, If not available.
```
pip install django
```
4. To create a new django project, let's say django_project; run
```
django-admin startproject django_project
``` 
5. Go inside the project and create app named testapp and then install it by tweaking settings.py inside the django_project directory. Basically, in the installed_apps list append testapp
```
cd django_project
python manage.py startapp testapp
```
6. Now, Inside the testapp directory create two directory static and templates. 
a. Inside templates, Create one more directory named testapp and then create a html file to render i.e index.html
b. Inside static, Create nested directory inside it with names testapp and css. Create a style.css inside it. Parallel to css directory, Create a folder named images too.

7. To create a index.html, backed with style.css which renders the image with it. Follow the steps
a. Open index.html, press ! then a basic template shall be created in the file.
b. The style.css's loading will be done by {% load static %} and then
<link rel="stylesheet" href= {% static 'testapp/css/style.css' %}">
c. Load the image by img tag by attaching src to it
<img src="{% static 'testapp/images/test.jpg' %}" alt="">
d. The html file is ready to render.

8. Write a view by writing the method in views.py located in the testapp directory

```
def index_page(request):
    return render(request, 'testapp/index.html')
```

9. Create a url path to access this via urls.py. Create this in testapp directory.

```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page) # at blank, render index_page
]

```

9. It is mandatory to create redirection from test app's urls.py to the central urls.py in the project
a. Add include in django.urls
b. add urlpatterns via 
path('', include('testapp.urls'))

10. create a css by going inside style.css and appending 
```
body{
    background-color: blue
}
```
11. Run the server in local host
``` 
python manage.py runserver
```
12. Create an app on heroku named test app via GUI, Then go to deploy section and connect Github to it.

13. Install the two packages - gunicorn and white noise
```
pip install gunicorn
pip install whitenoise
```
14. Then go to settings.py and set path to STATIC_ROOT by

```
STATIC_ROOT = os.path.join(BASE_DIR,'static')
```
15. Add MIDDLEWARE too
ie.
```MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]
```
16. Website to app will be name of app ie testapp.heroku.com

17. Add this to allowed_hosts in settings.py

```
ALLOWED_HOSTS = ['testapp.heroku.com']
```

18. Create Procfile in rootdir where manage.py is present
```
web: gunicorn demo.wsgi --log-file -
```

19. Make a text file of all dependencies via requirements.txt
```
pip freeze > requirements.txt
```
20. Connect the repository with app via choose branch to deploy and click deploy.
