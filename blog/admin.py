from django.contrib import admin
from blog.models import Post

## We need to register our model here in order to see it in the admin site
admin.site.register(Post)