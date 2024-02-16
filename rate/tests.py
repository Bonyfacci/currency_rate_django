from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Currency, CurrencyRate


class CurrencyViewsTestCase(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(
            charcode='USD', valuta_id='R01235', numcode=123, nominal=1, name='USA Dollar'
        )
        self.currency_rate = CurrencyRate.objects.create(
            currency=self.currency, date='2024-02-16', rate=12.3456
        )

    def test_currency_list_view(self):
        response = self.client.get(
            reverse('rate:currency_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_currency_rate_view(self):
        response = self.client.get(
            reverse('rate:currency_rate_list'),
            {'charcode': 'USD', 'date': '2024-02-16'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class CurrencyRateViewsTestCase(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(
            charcode='USD', valuta_id='R01235', numcode=123, nominal=1, name='USA Dollar'
        )
        self.currency_rate = CurrencyRate.objects.create(
            currency=self.currency, date='2024-02-16', rate=12.3456
        )

    def test_currency_rate_list_view(self):
        response = self.client.get(
            reverse('rate:currency_rate'),
            {'charcode': 'USD', 'date': '2024-02-16'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_currency_rate_detail_view(self):
        response = self.client.get(
            reverse('rate:currency_rate'),
            {'charcode': 'USD', 'date': '2024-02-16'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
