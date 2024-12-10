# HomePage/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Özel Kullanıcı Modeli
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

# Gönderi Modeli
class Post(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='homepage_posts'
    )
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return f'{self.user.username} - {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'


# Yorum Modeli
class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='homepage_comments', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='homepage_comments_users'
    )
    text = models.TextField(_("Comment Text"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f'{self.user.username} - {self.post.id}'
