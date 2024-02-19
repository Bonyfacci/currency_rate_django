from django.urls import path

from .apps import RateConfig
from .views import CurrencyRateListAPIView, CurrencyListAPIView, CurrencyRateAPIView, home, CurrencyListView, \
    CurrencyRateListView, CurrencyRateDetailView

app_name = RateConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('currency-list/', CurrencyListView.as_view(), name='currency-list'),
    path('currency-rates-list/', CurrencyRateListView.as_view(), name='currency-rate-list'),
    path('currency-rates/<int:currency_id>/', CurrencyRateDetailView.as_view(), name='currency-rate-detail'),

    path('currency/', CurrencyListAPIView.as_view(), name='currency_list'),
    path('currency_rates/', CurrencyRateListAPIView.as_view(), name='currency_rate_list'),

    path('rate/', CurrencyRateAPIView.as_view(), name='currency_rate'),
]
