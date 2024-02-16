import datetime
import logging

from celery import shared_task

from rate.services import CurrencyRateCBRF

logger = logging.getLogger(__name__)


@shared_task
def check_currency_rate():
    current_time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    print(f'Время сервера: {current_time}')

    logger.info(f"Получение курса валюты")

    data = CurrencyRateCBRF()

    logger.info(f"Получаем данные о курсах с сервиса ЦБ")
    data.rate_parser()
    logger.info(f"Записываем в базу данных")
    data.write_currency_and_rates_to_db()
    logger.info(f"Данные успешно обновлены")
