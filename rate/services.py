from datetime import datetime

import requests

from rate.models import Currency, CurrencyRate


class CurrencyRateCBRF:

    def __init__(self):
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        self.rates = None
        self.date = None

    def rate_parser(self):
        response = requests.get(self.url)
        self.rates = response.json()
        self.date = datetime.strptime(self.rates['Date'], '%Y-%m-%dT%H:%M:%S%z').date()

    def write_currency_and_rates_to_db(self):
        # Обновляем модель валют
        for charcode, info in self.rates['Valute'].items():
            if isinstance(info, dict):
                currency, created = Currency.objects.update_or_create(
                    charcode=charcode,
                    defaults={
                        'valuta_id': info.get('ID', ''),
                        'numcode': info.get('NumCode', 0),
                        'nominal': info.get('Nominal', 0),
                        'name': info.get('Name', ''),
                    }
                )
            else:
                print(f"Внимание: Информация для {charcode} не является словарём.")

            # Обновляем курсы валют в базе данных
            rate, created = CurrencyRate.objects.get_or_create(
                currency=currency,
                date=self.date,
                defaults={'rate': info.get('Value', 0)}
            )

            # Если курс валюты на указанную дату уже существует, обновляем его
            if not created:
                rate.rate = info.get('Value', 0)
                rate.save()

            print(f"Успешно обновлен курс {currency.charcode} до {info.get('Value', 0)} на {self.date}")
