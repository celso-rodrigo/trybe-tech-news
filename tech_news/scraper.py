import requests
from time import sleep


# Requisito 1
def fetch(url):
    """
    Deve receber uma URL
    Deve fazer uma requisição HTTP GET para esta URL utilizando requests.get
    Deve retornar o conteúdo HTML da resposta
    Deve respeitar um Rate Limit de 1 requisição por segundo
    Caso Status Code 200: OK, deve ser retornado seu conteúdo de texto
    Caso status diferente de 200, deve-se retornar None
    Caso não receba resposta em até 3 segundos, timeout e retorna None
    """

    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (
        requests.HTTPError,
        requests.ReadTimeout,
        requests.exceptions.Timeout,
    ):
        return None

    sleep(1)  # Rate limit
    return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
