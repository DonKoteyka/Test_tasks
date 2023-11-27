import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('API_URL')


def get_request(url):
    return requests.get(url).json()
