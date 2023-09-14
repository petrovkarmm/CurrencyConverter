import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

headers = {
    "apikey": os.getenv('api_key')
}


def currency_convert(current_currency, to_currency, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={current_currency}&amount={amount}"

    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result_json = response.json()

    result_value = result_json.get('result')

    return result_value
