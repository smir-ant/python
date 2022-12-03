import requests

response = requests.get(url="https://api.kanye.rest")
quote = response.json()["quote"]
print(quote)