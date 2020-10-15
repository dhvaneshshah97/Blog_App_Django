from django.db.models.signals import post_save  ## this signal will be fired after an object is saved
from django.contrib.auth.models import User  ## the User model is going to be sender
from django.dispatch import receiver ## a receiver is function that gets signal and then perform some tasks
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()