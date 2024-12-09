from django.db import models

# Create your models here.
class CustomUser(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)