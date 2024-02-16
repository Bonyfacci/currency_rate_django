from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class LowerCaseEmailField(models.EmailField):
    """
    Модель почты пользователя
    """

    def get_prep_value(self, value):
        if value:
            return str(value).lower()
        return None


class User(AbstractUser):
    """
    Модель пользователя
    """

    email = LowerCaseEmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('pk',)
