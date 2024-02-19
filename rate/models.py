from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Currency(models.Model):
    """
    Модель валюты
    """
    charcode = models.CharField(max_length=3, unique=True, verbose_name="Буквенный код")

    valuta_id = models.CharField(max_length=10, **NULLABLE, verbose_name='ID валюты')
    numcode = models.PositiveIntegerField(**NULLABLE, verbose_name='Цифровой код')
    nominal = models.PositiveIntegerField(**NULLABLE, verbose_name='Единиц')
    name = models.CharField(max_length=100, **NULLABLE, verbose_name='Валюта')

    def __str__(self):
        return f'{self.charcode}'

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ('charcode',)


class CurrencyRate(models.Model):
    """
    Модель курса валюты.
    """
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Код валюты')
    date = models.DateField(verbose_name="Дата установки курса")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс валюты в рублях")

    def __str__(self):
        return f'{self.currency} - {self.date} - {self.rate} рублей'

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        ordering = ('-date',)
