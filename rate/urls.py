from django.urls import path

from .apps import RateConfig
from .views import CurrencyRateListAPIView, CurrencyListAPIView, CurrencyRateAPIView

app_name = RateConfig.name

urlpatterns = [
    path('currency/', CurrencyListAPIView.as_view(), name='currency_list'),
    path('currency_rates/', CurrencyRateListAPIView.as_view(), name='currency_rate_list'),

    path('rate/', CurrencyRateAPIView.as_view(), name='currency_rate'),
]
