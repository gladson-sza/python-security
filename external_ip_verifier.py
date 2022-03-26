import re
import json
from urllib.request import urlopen


if __name__ == '__main__':
    url = 'https://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    print(data)

