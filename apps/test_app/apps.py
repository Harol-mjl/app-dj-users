from django.apps import AppConfig
from apps import test_app


class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.test_app'
