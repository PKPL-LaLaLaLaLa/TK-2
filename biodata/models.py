from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bg_color = models.CharField(max_length=20, default='#0f0f1a')
    card_color = models.CharField(max_length=20, default='#1a1a2e')
    accent_color = models.CharField(max_length=20, default='#e94560')
    font_family = models.CharField(max_length=100, default='Syne')
    text_color = models.CharField(max_length=20, default='#ffffff')

    def __str__(self):
        return f"Preference - {self.user.username}"