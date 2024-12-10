from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.feed_page, name='feed_page'),
]
