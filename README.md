# Parser-Site

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/requests-HTTP-2A6DB2)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML-4B8BBE)

Учебный парсер интернет-магазина на Python: скачивает страницу каталога и вытаскивает из карточек товаров название, ссылку на картинку и код товара.

## Что умеет
- Загружает страницу каталога (в примере — раздел IP-камер магазина alser.kz) с заголовками обычного браузера.
- Находит на странице все карточки товаров.
- Для каждого товара выводит **название**, **ссылку на изображение** и **код товара**.

## Стек
- **Python 3**
- **requests** — загрузка страницы
- **BeautifulSoup 4** — разбор HTML

## Как запустить

```bash
git clone https://github.com/MarlenGO/Parser-Site.git
cd Parser-Site
pip install requests beautifulsoup4
python main.py
```

> Учебный проект 2021 года: сайт с тех пор мог поменять вёрстку, и тогда классы в `main.py` нужно обновить.
