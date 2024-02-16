import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class ValueConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "kSShf0UHdCczGrjNifzn7u1YKsHSFwQk"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        total_base = json.loads(response.content)['result']

        return total_base
