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
    # Soft pink + purple hint default theme
    bg_color = models.CharField(max_length=20, default='#FCF8F8')
    card_color = models.CharField(max_length=20, default='#FBEFEF')
    accent_color = models.CharField(max_length=20, default='#F5AFAF')
    font_family = models.CharField(max_length=100, default='Outfit')
    text_color = models.CharField(max_length=20, default='#4a044e')

    def __str__(self):
        return f"Preference - {self.user.username}"