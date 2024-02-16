from django.core.management.base import BaseCommand

from rate.services import CurrencyRateCBRF


class Command(BaseCommand):
    help = 'Update currency rates from CBRF service'

    def handle(self, *args, **options):
        data = CurrencyRateCBRF()
        # Получаем данные о курсах с сервиса ЦБ
        data.rate_parser()
        # Записываем в базу данных
        data.write_currency_and_rates_to_db()
