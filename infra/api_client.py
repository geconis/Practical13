import requests

BASE_URL = "https://genshin.jmp.blue"

class GenshinAPIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_characters(self):
        url = f"{self.base_url}/characters"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_character(self, name):
        url = f"{self.base_url}/characters/{name}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_weapons(self):
        url = f"{self.base_url}/weapons"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
