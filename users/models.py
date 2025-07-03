from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_ROLES = (
        ("admin", "Admin"),
        ("standard", "Standard User"),
        ("guest", "Guest"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default="standard")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    def __str__(self):
        return self.user.username
