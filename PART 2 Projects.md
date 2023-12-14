# Alien Invasion: Making a Game with Python
## Chapter 12: A Ship that Fires Bullets
## Chapter 13: Aliens!
## Chapter 14: Scoring
---
---
# Data Visualization
## Chapter 15: Generating Data
## Chapter 16: Downloading Data
## Chapter 17: Working with APIs
---
---
# Web Applications
## Chapter 18: Getting Stated with Django

* Setting Up a Project
* Starting an App
* Making Pages: The Learning Log Home Page
* Building Additional Pages

#### Setting Up a Project
* spec
* Creating a Virtual Environment
  * `python3 -m venv env_name`
  * `python3 -m venv venv --promt="env_name"`
* Activating and Deactivating virtual environment
* `pip install package-name` inside venv
* `django-admin startproject project-name .` - to start a project
* `python3 manage.py migrate` - to create SQLite database
* `python3 manage.py runserver`

#### Starting an App
* `python3 manage.py startapp app-name` to create an app
* models.py
    ```python
    from django.db import models
    class Topic(models.Model):
        """A topic the user is learning about."""
        text = models.CharField(max_length=200)
        date_added = models.DateTimeField(auto_now_add=True)
        
        def __str__(self): # similar to toString() in Java
            """Return a string representation of the model."""
            return self.text
    ```
* Activate models by including the app in the `INSTALLED_APPS` list in _settings.py_
  * Group apps by `# My apps` & `# Default django apps` and place custom apps before default apps to override any behaviour
  * `python3 manage.py makemigrations app-name` to make modifications in the database as per the models
  * `python3 manage.py migrate` to apply the changes
* _admin site_
  * `python3 manage.py createsuperuser` to create a super user
* Register a model with the Admin site by modifying the _admin.py_
    ```python
    from django.contrib import admin
    from .models import Topic
    admin.site.register(Topic)
    ```

---

## Chapter 19: User Accounts

* 
## Chapter 20: Styling and Deploying an App
---
---