# ProfilePage/urls.py
from django.urls import path
from . import views

app_name = 'profile'  # URL ad alanını tanımlayın

urlpatterns = [
    path('profile_page/', views.profile_page, name='profile_page'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),  # Yeni eklenen URL
]
