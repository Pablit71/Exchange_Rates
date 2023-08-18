import json
from datetime import datetime

import requests
from django.core.management.base import BaseCommand

from currency_app.models import Currency, CurrencyRate


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = json.loads(response.text)
        date_str = data['Date']
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S+03:00').date()

        for key, val in data['Valute'].items():
            char_code = val['CharCode']
            name = val['Name']
            value = val['Value']

            currency, _ = Currency.objects.get_or_create(char_code=char_code, name=name)
            CurrencyRate.objects.update_or_create(currency=currency, date=date, defaults={'value': value})

        self.stdout.write(self.style.SUCCESS('Курсы валют успешно обновлены'))
