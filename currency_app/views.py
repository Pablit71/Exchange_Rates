import json

from django.http import HttpResponse

from currency_app.models import CurrencyRate


def show_rates(request):
    date = request.GET.get('date')
    rates = CurrencyRate.objects.filter(date=date)
    result = {rate.currency.name: str(rate.value) for rate in rates}
    response_data = json.dumps(result, ensure_ascii=False)
    return HttpResponse(response_data, content_type="application/json; charset=utf-8")

