import requests

url = "https://opentdb.com/api.php"
parameters = {
    'amount': 100,
    'type': 'boolean'
}

request = requests.get(url, params=parameters)
request.raise_for_status()

question_data = request.json()["results"]

