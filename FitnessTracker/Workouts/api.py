import requests


def get_exercises():
    url = "https://wger.de/api/v2/exercise/"
    headers = {
        "Authorization": "19ddb99c4e3e444fc6c90bba094f7391a5e46d52"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    return data
