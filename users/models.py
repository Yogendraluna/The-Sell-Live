from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    location = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False, help_text="Contact Number")