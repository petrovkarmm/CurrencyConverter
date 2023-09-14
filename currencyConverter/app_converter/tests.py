from django.test import TestCase
from .models import CurrencyRate


class CurrencyRateTestCase(TestCase):
    def setUp(self):
        # Создаем запись в модели CurrencyRate для тестирования
        self.currency_rate = CurrencyRate.objects.create(
            from_currency='USD',
            to_currency='EUR',
            rate=0.85
        )

    def tearDown(self):
        self.currency_rate.delete()

    def test_get_rate(self):
        # Проверяем, что значение курса обмена получается корректно
        rate = CurrencyRate.objects.get(from_currency='USD', to_currency='EUR').rate
        self.assertEqual(rate, 0.85)
