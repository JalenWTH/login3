# login3
The third iteration of my authorization practice projects. This one features cleaner class-based views instead of function-based views and Django's LoginRequiredMixin.

## How to run it:

This text assumes you already have Python and the pip package manager installed on your device

This app only requires Django and Python

### Django installation

From your command line, change directories to the directory of your Python installation, and run the pip installation:

`pip install django==4.0.4`

To view your Django version and make sure the installation worked, run:

`django-admin --version`

### Generating the Django project and files

In any directory you want, run this command from the command line:

`django-admin startproject projectname [directory]`

The directory portion may be left blank if you want the project generated in place. This generates a new directory with all of your project files. Your project files are actually in a subdirectory of that directory with the same name. 

`python manage.py startapp crud`

This generates your app files. Next, go into your project directory and find your settings.py file. You'll need to add your ap to the installed apps list like:

```
installed_apps=[
...,
'crud',
...
]
```

### urls.py 

You need to change your urls.py file for your **project** to tell it to include url patterns for the crud app. Keep in mind that there will also be urls.py for your **app** later. Add this code:

```
from django.urls import path, include

path('admin/', admin.site.urls),
path('crud/', include('crud.urls')
```

This will make sure that all url patterns from your app urls.py file are included and every path for the crud app starts with 'crud/'. After this, copy over the app files from this repository. You'll need to create some of them (urls.py, templates) along with some new directories. This is the app directory structure

```
crud 
  urls.py
  views.py
  models.py
  admin.py
  templates dir
    login3 dir <!-- important -->
      base.html
      home.html
      login.html
      signup.html
 ```
    
      
    
    
