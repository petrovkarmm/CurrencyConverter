import unittest
from django.test import Client
from APILayer.fixer_api import currency_convert


class CurrencyConvertFunctionTestCase(unittest.TestCase):
    def test_apiLayer_currency_convert(self):
        current_currency = 'USD'
        to_currency = 'EUR'
        amount = 10

        result = currency_convert(current_currency, to_currency, amount)

        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)


class GetCurrencyRateTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_currency_rate(self):
        response = self.client.get('/api/rates/', {'from': 'USD', 'to': 'EUR', 'value': 10})

        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())


class GetCurrencyRateSameCurrencyTestCase(unittest.TestCase):
    # Тест на конвертацию одинаковых валют
    def setUp(self):
        self.client = Client()

    def test_get_currency_rate_same_currency(self):
        response = self.client.get('/api/rates/', {'from': 'USD', 'to': 'USD', 'value': 10})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())


class GetCurrencyRateWrongParamsTestCase(unittest.TestCase):
    # Тест на конвертацию с ошибками в параметрах
    def setUp(self):
        self.client = Client()

    def test_get_currency_rate_wrong_params_value (self):
        response = self.client.get('/api/rates/', {'from': 'USD', 'to': 'EUR', 'value': 'fail'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())

    def test_get_currency_rate_wrong_params_from(self):
        response = self.client.get('/api/rates/',
                                   {'from': 'fail', 'to': 'RUB', 'value': 10})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())

    def test_get_currency_rate_wrong_params_ro(self):
        response = self.client.get('/api/rates/',
                                   {'from': 'USD', 'to': 'fail', 'value': 10})

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())
