from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    cost = models.IntegerField()
    liked_by = models.ManyToManyField('CustomUser', related_name = 'liked_trips')

class CustomUser(AbstractUser):
 
    email = models.EmailField(_('email address'), unique = True)
    preferred_travel_dates = models.DateField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    preferred_activities = models.CharField(max_length=255, null=True, blank=True)   
    
    saved_trips = models.ManyToManyField(Trip, related_name='saved_by')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    profile_pic_thumbnail = ImageSpecField(source='profile_pic',
                                            processors=[ResizeToFill(100, 100)],
                                            format='JPEG',
                                            options={'quality': 60})
    
    bio = models.TextField(max_length = 500, blank = True)
    following = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')