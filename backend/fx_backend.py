import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = os.getenv('api_key')
currencies = input(str("What currency?: "))

url = f"https://api.currencyapi.com/v3/latest?apikey={headers}&currencies={currencies}"

response = requests.get(url)
print(headers)
print(url)
print(response.text)
