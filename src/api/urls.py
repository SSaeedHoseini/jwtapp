"""urls for api module"""
from django.urls import path
from .views import json_web_token_auth

urlpatterns = [
    path('token/', json_web_token_auth)
]
