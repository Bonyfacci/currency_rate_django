from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import CurrencyRate, Currency
from .serializers import CurrencyRateSerializer, CurrencySerializer
from datetime import datetime


class CurrencyListAPIView(ListAPIView):
    """
    API View для получения списка валют.

    Пример запроса:
    http://127.0.0.1:8000/currency/

    Пример успешного ответа:
    [
        {
        "valuta_id": "R01230",
        "numcode": 784,
        "charcode": "AED",
        "nominal": 1,
        "name": "Дирхам ОАЭ"
        },
        {
            "valuta_id": "R01060",
            "numcode": 51,
            "charcode": "AMD",
            "nominal": 100,
            "name": "Армянских драмов"
        },
        # ... другие валюты
    ]
    """

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CurrencyRateListAPIView(ListAPIView):
    """
    API View для получения списка курсов валют на указанную дату.

    Параметры запроса:
    - date: Дата в формате YYYY-MM-DD.

    Пример запроса:
    http://127.0.0.1:8000/currency_rates/
    http://127.0.0.1:8000/currency_rates/?date=2024-01-01

    Пример успешного ответа:
    [
        {
        "charcode": "AUD",
        "date": "2024-02-16",
        "rate": "59.5477"
        },
        {
            "charcode": "AZN",
            "date": "2024-02-16",
            "rate": "54.0139"
        },
        # ... другие курсы валют на указанную дату
    ]
    """

    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        date_param = self.request.query_params.get('date', None)

        if date_param:
            try:
                date_obj = datetime.strptime(date_param, '%Y-%m-%d').date()
            except ValueError:
                return CurrencyRate.objects.none()

            queryset = CurrencyRate.objects.filter(date=date_obj)

            if not queryset.exists():
                return CurrencyRate.objects.none()
        else:
            queryset = CurrencyRate.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"error": "Данные на указанную дату не обнаружены. Пожалуйста, повторите запрос."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CurrencyRateAPIView(APIView):
    """
    API View для получения курса валюты на указанную дату.

    Параметры запроса:
    - charcode: Код валюты (например, "AUD").
    - date: Дата в формате YYYY-MM-DD.

    Пример запроса:
    http://127.0.0.1:8000/rate/?charcode=AUD&date=2024-02-16

    Пример успешного ответа:
    {
        "charcode": "AUD",
        "date": "2024-01-01",
        "rate": 57.0627
    }
    """

    def get(self, request, *args, **kwargs):
        charcode = request.query_params.get('charcode')
        date = request.query_params.get('date')

        # Проверка наличия параметров charcode и date в запросе
        if not charcode or not date:
            return Response({"error": "Параметры charcode и date обязательны."}, status=400)

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Неверный формат даты. Используйте формат YYYY-MM-DD."}, status=400)

        currency = get_object_or_404(Currency, charcode=charcode.upper())
        rate = get_object_or_404(CurrencyRate, currency=currency, date=date_obj)

        data = {
            "charcode": rate.currency.charcode,
            "date": str(rate.date),
            "rate": float(rate.rate)
        }

        return Response(data)


def home(request: HttpRequest) -> HttpResponse:
    """
    Домашняя страница
    :param request: {method},
    :return: HttpResponse
    """
    currencies = Currency.objects.all()
    selected_currency_id = request.POST.get('currency', None)

    if selected_currency_id:
        selected_currency = Currency.objects.get(id=selected_currency_id)
        currency_rate = CurrencyRate.objects.filter(currency=selected_currency).first()
    else:
        currency_rate = None

    return render(
        request,
        template_name='rate/home.html',
        context={'currencies': currencies, 'currency_rate': currency_rate},
    )


class CurrencyListView(ListView):
    """
    Представление для списка валют.
    Выводит список всех доступных валют.
    """
    model = Currency
    serializer_class = CurrencySerializer


class CurrencyRateListView(ListView):
    """
    Представление для списка курсов валют.
    Выводит список всех доступных курсов валют.
    """
    model = CurrencyRate
    serializer_class = CurrencyRateSerializer


class CurrencyRateDetailView(DetailView):
    """
    Представление для детальной информации о курсе валюты.
    Выводит детальную информацию о курсе валюты по заданному идентификатору.
    """
    model = CurrencyRate
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset
