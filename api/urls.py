from django.contrib import admin
from django.urls import path
from .views import API
urlpatterns = [
    path('api/' ,API.as_view()),
]