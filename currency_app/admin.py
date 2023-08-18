from django.contrib import admin

from .models import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('char_code', 'name')


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'value')
    ordering = ('value',)  # Сортировка по умолчанию от меньшего к большему

    def get_ordering(self, request):
        if request.GET.get('o') == 'value':
            return ['value']
        elif request.GET.get('o') == '-value':
            return ['-value']
        return super(CurrencyRateAdmin, self).get_ordering(request)
