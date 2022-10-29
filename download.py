# download.py

import requests
import os
import urllib.request

def download_image(url, path):
    response = requests.get(url)
    urllib.request.urlretrieve(url, os.path.dirname(__file__) + "\\" + path)

    return True
    