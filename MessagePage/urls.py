from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.message_page, name='message_page'),
]
