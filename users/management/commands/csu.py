from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from users.models import User

from config.settings import ADMIN_EMAIL, ADMIN_PASSWORD


class Command(BaseCommand):
    """
    Команда для создания супер пользователя
    """

    def handle(self, *args, **options):

        if ADMIN_EMAIL and ADMIN_PASSWORD:
            password = make_password(ADMIN_PASSWORD)
            data = {
                'username': ADMIN_EMAIL,
                'is_active': True,
                'is_staff': True,
                'is_superuser': True,
                'password': password,
            }
            User.objects.update_or_create(email=ADMIN_EMAIL, defaults=data)
