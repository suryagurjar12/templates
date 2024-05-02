from django.urls import path 
from .views import *

urlpatterns =[
    path("",home2, name="home")
]