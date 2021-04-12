from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("",views.Index,name="index"),
    path("submit",views.Submit,name="submit"),
     
]
 