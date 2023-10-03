from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    followers = models.ManyToManyField(
        User,
        related_name="followings",
    )
    bio = models.CharField(max_length=1000)

