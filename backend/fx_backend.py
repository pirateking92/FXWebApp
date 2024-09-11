import requests # for http requests
import os # so that i can load the .env
from dotenv import load_dotenv

load_dotenv() # does what it says on the tin

headers = os.getenv('api_key')
currencies = input(str("What currency?: "))

url = f"https://api.currencyapi.com/v3/latest?apikey={headers}&currencies={currencies}"

response = requests.get(url)
print(headers)
print(url)
print(response.text)


