from django.db import models


class CurrencyRate(models.Model):
    from_currency = models.CharField(max_length=3, verbose_name='Из данной валюты')
    to_currency = models.CharField(max_length=3, verbose_name='В текущую валюту')
    rate = models.FloatField(verbose_name='Коэффициент')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.from_currency} -> {self.to_currency}"
