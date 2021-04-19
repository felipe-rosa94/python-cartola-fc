import requests

URL_BASE = 'https://api.cartolafc.globo.com/'


def get(params):
    response = requests.get(URL_BASE + params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Erro ao cunsumir API.'