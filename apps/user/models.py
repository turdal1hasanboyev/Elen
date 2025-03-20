from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel
from .managers import CustomUserManager


class CustomUser(BaseModel, AbstractUser):
    """Custom User model."""

    """
    Fields:

    username = None
    first_name = (null=True, blank=True)
    last_name = (null=True, blank=True)
    email = (unique=True)
    """

    username = None
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(blank=True, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta class."""

        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Return string representation of user."""

        return f"{self.email}"
