from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [
   
    path('<str:ProfileName>',views.FindProfileByName,name='find_profile_by_name'),
    path('',views.DefaultProfilePage,)
]
