"""urls for api module"""
from django.urls import path
from .views import JSONWebTokenAuth, SayHelow

urlpatterns = [
    path('token/', JSONWebTokenAuth.as_view()),
    path('sayhelow/', SayHelow.as_view())
]
