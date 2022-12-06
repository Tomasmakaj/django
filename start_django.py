# Creating a virtual environment to work with Django
python3 -m venv 11_env

# To Activate the Virtual Environment
source 11_env/bin/activate

# If your using Powershell without the word source to activate the virtual environment you might need to capitalize Activate

# To Stop using virtual environment enter
deactivate

# Install Django once the environment is activarted enter:
pip3 install django or pip install django

# Creating a project in Django (remember to look for the 11_env in parentheses)
django-admin startproject learning_log .

# This command tells Django to set up a new project called learning_log 
# The dot at the end of the command creates the new project with a directory structure that will make it easy to deploy the app to a server when finished
# Dont forget the dot if you forget delete the files and folders that were created and run the command again with the dot

# Creating the Database
python manage.py migrate
# Anytime we modify a database, we're migrating the database. Issuing the migrate command for the first time tells
# Django to make sure the database matches the current state of the project.
# The first time we run this command in a new project we create SQLite. 

# Viewing the Project
python manage.py runserver
# Django should start a server called development server

# To stop the server
Press control c in the terminal

# If you receive a message that the port is already in use tell Django to use a different port by entering
# manage.py runserver 8001
# And the cycle through the high numbers until you find an open port.

# Starting an App
source 11_env/bin/activate
python manage.py startapp learning_logs
# The command startapp appname tell Django to create the infrastructure needed to build an app.
# The most important files created are models.py, admin.py, and views.py
# We will use models to define the data we want to manage in our app

# Defining Models
from django.db import models

# Create your models here.
class Topic(models.Model):
    """A Topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add==True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# We've created a class called Topic, which inherits from Model a parent included in Django that defines a moddel's basic functionality
# We add two attributes to the Topic class: text and date_added
# The text attribute is CharField a piece of data that's made up of characters or text.
# You use CharField when you want to store a small amount of text, such as a name, a title or a city
# We define a CharField attribute we have to tell Django how much space it should reserve in the database.
# We give it a max length of 200 characters

# The date_added attribute is a DateTimeField a piece of data that will record a date and time.
# We pass the argument auto_now_add=True which tell Django to automatically set the attribute to the current date and time 
# Whenever a topic is created

# We tell Django which attribute to use by defualt when it displays information about a topic. Django calls a __str__() method
# to display a simple representation of a model. Here we've written a method that returns the string stored in the text attribute


# Activating Models
# To use our models, we have to tell Django to inclue our app in the overall project. Open settings.py you'll see a section that tells
# Django which apps are installed and work together
# We add our app to this list by modifying INSTALLED_APPS

INSTALLED_APPS = [
    # My app
    "learning_logs",
    
    # Default django apps.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Next we need to tell Django to modify the database so it can store information related to the model Topic
python manage.py makemigrations learning_logs

# The command makemigrations tell Django to figure out how to modify the database so it can store the data associated with any new models we've defined
# This migration will create a table for the model Topic in the database.

# Now we will apply this migration and have Django modigy the database for us.
python manage.py migrate


# Anytime we want to modify the data the Learning Log manages follow these steps
# Modify models.py,
# Call makemigrations on learning_logs
# Tell Django to migrate the project


# The Django Admin Site

# Crearing a superuser
# Django allows you to create a superuser, a user who has all privileges available on the site.
python manage.py createsuperuser

# Registering a Model with the Admin Site

from django.contrib import admin

# Register your models here.

from .models import Topic

admin.site.register(Topic)


# Defining the entry Model
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
    
# Migrating the Entry Model

python manage.py makemigrations learning_logs
python manage.py migrate


# Registering Entry with the Admin Site
from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)