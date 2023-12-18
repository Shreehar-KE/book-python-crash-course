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
  * `python3 -m venv venv --prompt="env_name"`
* Activating and Deactivating virtual environment
* `pip install package-name` inside venv
* `django-admin startproject project-name .` - to start a project
  * dot(.) at the end
* `python3 manage.py migrate` - to create SQLite database
* `python3 manage.py runserver`

#### Starting an App
* Django project : group of individual apps
* `python3 manage.py startapp app-name` to create an app
* models.py - to define models
* _models_ tels django how to work with the data
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
  ```python
  INSTALLED_APPS = [
      # My apps.
      'learning_logs',
      # Default django apps.
      'django.contrib.admin',
      #--snip--
  ]
  #--snip--
  ```
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
* Adding topics using the admin site
* many-to-one relationship
  ```python
  from django.db import models
  class Topic(models.Model):
  #--snip--
  class Entry(models.Model):
      """Something specific learned about a topic."""
      topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
      text = models.TextField()
      date_added = models.DateTimeField(auto_now_add=True)
  
      class Meta:
          verbose_name_plural = 'entries'

      def __str__(self):
          """Return a simple string representing the entry."""
          return f"{self.text[:50]}..."
  ```
* foreign key
* cascading delete
* Django shell
  * foreign key relationship `_set`

#### Making Pages: The Learning Log Home Page
* defining URLs, writing views and writing templates
* URL Pattern - routing
* mapping a URL using _urls.py_ in main project folder
  * `urlspatterns` list
  * `include()` function
  * creating new _urls.py_ in app folder
      ```python
      """Defines URL patterns for learning_logs"""

      from django.urls import path

      from . import views

      app_name = 'learning_logs'
      urlpatterns = [
          # Home page
          path('', views.index, name='index'),
      ]
      ```
      * app_name
      * `path()` function call
      * `index()` function in _views.py_ 
      * _name_ argument
* A view function takes in information from a request, prepares the data needed to generate a page
  * `render()` function
  * `request` object
  * template argument
* The template defines what the page should look like, and Django fills in the relevant data each time the page is requested
  * _templates_ folder
    * _app-folder/templates/app-name/index.html_

#### Building Additional Pages
* Template Inheritance
  * _base.html_ - base template
    ```html
    <p>
      <a href="{% url 'learning_logs:index' %}">Learning Log</a>
    </p>
    {% block content %}{% endblock content %}
    ```
  * template tag `{% %}`
  * block tags
    ```
    {% block content %}

    {% endblock content %}
    ```
  * child template
  * extends tag `{% extends %}`
* `{% for %}`
* `{{variable}}`
* `{%empty%}`
* *learning_logs/urls.py*
  ```python
    #--snip--
    urlpatterns = [
    #--snip--
    # Detail page for a single topic.
      path('topics/<int:topic_id>/', views.topic, name='topic'),
    ]
  ```
* _views.py_
  ```python
    #--snip--   
    def topic(request, topic_id):
        """Show a single topic and all its entries."""
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)
  ```
* queries - `Topic.objects.get(id=topic_id)`
* | represents a template filter function 
* _topic.html_
  ```html
    {% extends 'learning_logs/base.html' %}
    {% block content %}
      <p>Topic: {{ topic.text }}</p>
      <p>Entries:</p>
      <ul>
        {% for entry in entries %}
          <li>
            <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
            <p>{{ entry.text|linebreaks }}</p>
          </li>
        {% empty %}
          <li>There are no entries for this topic yet.</li>
        {% endfor %}
      </ul>
    {% endblock content %}
  ```
* _topics.html_
  ```html
  --snip--
    {% for topic in topics %}
      <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">
          {{ topic.text }}
        </a>
      </li>
    {% empty %}
  --snip--
  ```
---

## Chapter 19: User Accounts

* 
## Chapter 20: Styling and Deploying an App
---
---