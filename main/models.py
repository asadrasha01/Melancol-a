from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here (e.g., preferences, booking history, etc.)
    email = models.EmailField(_('email address'), unique = True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
