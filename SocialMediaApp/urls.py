# SocialMediaApp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomePage.urls', namespace='home')),  # Ana sayfa yönlendirme
    path('login/', auth_views.LoginView.as_view(template_name='HomePage/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', include('ProfilePage.urls', namespace='profile')),  # Profil URL'leri
]
# Medya dosyalarını sunmak için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)