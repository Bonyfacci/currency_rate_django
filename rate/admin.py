from django.contrib import admin

from rate.models import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyListAdmin(admin.ModelAdmin):
    list_display = ('charcode', 'name', 'valuta_id', 'numcode', 'nominal')
    search_fields = ('charcode', 'name')


@admin.register(CurrencyRate)
class CurrencyRateListAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'rate')
    search_fields = ('currency__charcode', 'date')
    list_filter = ('currency', 'date')
    ordering = ('-date', 'currency')
