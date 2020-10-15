from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) ## inheriting User model, if user is deleted, profile is deleted, but not the vice-versa
    image = models.ImageField(default = 'default.jpg', upload_to = "profile_pics") ## default for default image, profile_pics is directory that images get uploaded to

    ## display Profile object how we want it to display
    def __str__(self):
        return f"{self.user.username} Profile"
