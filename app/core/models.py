"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manage for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

<<<<<<< HEAD
=======

>>>>>>> 4389094 (Create User Model)
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects: UserManager()

<<<<<<< HEAD
    USERNAME_FIELD = 'email' #defines the field that we want to use for authentication
=======
    USERNAME_FIELD = 'email'   # defines the field that we want
                               # to use for authentication  # noqa
>>>>>>> 4389094 (Create User Model)
