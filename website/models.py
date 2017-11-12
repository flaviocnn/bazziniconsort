from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=700, blank=True)
    location = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/profiles', default='images/profiles/empty.jpg')
    def __str__(self):
            return self.user.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@python_2_unicode_compatible    
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, default='...')
    image_url = models.ImageField(upload_to='images/events', default='images/events/empty.jpg')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
