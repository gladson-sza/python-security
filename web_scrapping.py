from bs4 import BeautifulSoup

import requests

if __name__ == '__main__':
    site = requests.get('https://www.climatempo.com.br/').content

    soup = BeautifulSoup(site, 'html.parser')

    print(soup.title.string)

