from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: '+XXXXXXXXX'. Max 15 digits.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    email_address = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    
class User(models.Model):
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    