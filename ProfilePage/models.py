# ProfilePage/models.py
from django.db import models
from HomePage.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='profile_posts'
    )
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
