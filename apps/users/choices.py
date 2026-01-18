from django.db import models

class UserRoleChoices(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    USER = 'USER', 'User'
    GUEST = 'GUEST', 'Guest'
