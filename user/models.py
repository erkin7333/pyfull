from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from pyfull.validators import PhoneValidator
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass

class User(AbstractUser):
    objects = UserManager()

    # password = models.CharField(('password'), max_length=128)
    phone = models.CharField(max_length=15, unique=True, default=None, null=True,
                             validators=[PhoneValidator()])


