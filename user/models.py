from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from pyfull.validators import PhoneValidator
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass

class User(AbstractUser):
    objects = UserManager()

    phone = models.CharField(max_length=15, unique=True, default=None, null=True,
                             validators=[PhoneValidator()])
    group_name = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)

