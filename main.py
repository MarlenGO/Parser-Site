import requests
from bs4 import BeautifulSoup

# Ссылка для парсинга
URL = 'https://alser.kz/c/ip-kamery'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': '*/*'
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
cards = soup.findAll('div', class_ = 'product-item')
blocks = []

for card in cards:
    blocks.append({
        'img': card.find('a', class_ = 'product-item__image').find('img').get('src'),
        'title': card.find('a', class_ = 'product-item__info_title'),
        'cod_tovar': card.find('li', class_ = 'product-item__tooltip').get('data-title')
    })

    for block in blocks:
        print('Название: ', block['title'].text)
        print('Ссылка на картинку: ', block['img'])
        print(block['cod_tovar'])