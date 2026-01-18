from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.choices import UserRoleChoices


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.USER,
    )
    def __str__(self):
        return f'{self.username} ({self.role})'