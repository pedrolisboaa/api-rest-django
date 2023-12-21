import requests


url = "http://localhost:8000/api/habilidade"

dados = [
    {"nome": None},
    {"nome": "Azure"},
    {"nome": "AWS"},
    {"nome": "Google Cloud"}
]

for dado in dados:
    response = requests.post(url, json=dado)
    print(response.status_code, response.json())
    

