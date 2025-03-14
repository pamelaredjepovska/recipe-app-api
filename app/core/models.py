"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """Manager for User objects."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """A user in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # Assign a UserManager

    USERNAME_FIELD = 'email' # The field used for authentication, replace the default one
