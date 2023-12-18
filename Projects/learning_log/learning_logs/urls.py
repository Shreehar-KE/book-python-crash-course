"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to list all topics added to Learning Log
    path('topics/', views.topics, name="topics"),
    # Individual Page for each Topic where all the Entries are listed
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
