from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=3, verbose_name="Код валюты")
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валюта")
    date = models.DateField(verbose_name="Дата сбора данных")
    value = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Значение")

    def __str__(self):
        return f"{self.currency} - {self.date}"

    class Meta:
        unique_together = ('currency', 'date')
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
