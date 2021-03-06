import requests
import json


api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=9134ad4d-3ba1-4017-85b1-c5ec86a2a50a")
print(api_request)
# düzgün formatta alabilmek için
result = json.loads(api_request.content)
print(result)
