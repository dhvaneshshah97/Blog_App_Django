from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


## Post model ## we need to run migrations to update the database with any changes
## Since we create a Post model, thereby make change to database, so we need to run migrations

## You need to run migrate command to actually create a table
class Post(models.Model):
    # fields of our table/model
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title