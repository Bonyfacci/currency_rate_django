from rest_framework import serializers

from rate.models import Currency, CurrencyRate


class CurrencySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Currency.

    Пример сериализованных данных:
    {
        "valuta_id": "R01230",
        "numcode": 784,
        "charcode": "AED",
        "nominal": 1,
        "name": "Дирхам ОАЭ"
    }
    """

    class Meta:
        model = Currency
        fields = ('valuta_id', 'numcode', 'charcode', 'nominal', 'name')


class CurrencyRateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CurrencyRate.

    Пример сериализованных данных:
    {
        "charcode": "AUD",
        "date": "2024-02-16",
        "rate": 59.5477,
    }
    """

    charcode = serializers.SerializerMethodField()

    class Meta:
        model = CurrencyRate
        fields = ('charcode', 'date', 'rate')

    def get_charcode(self, obj):
        return obj.currency.charcode
