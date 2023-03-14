import requests
import re
from time import sleep
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    """
    Deve receber uma string com o conteúdo HTML da página inicial do blog
    Deve fazer o scrape do conteúdo e obter uma lista de URLs das notícias
    Deve retornar uma lista de URLs das notícias dos cards
    Caso não encontre nenhuma URL de notícia, retornar uma lista vazia
    """

    soup = BeautifulSoup(html_content, "html.parser")
    urls = [
        anchor.get("href")
        for anchor in soup.find_all("a", {"class": "cs-overlay-link"})
    ]

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """
    Deve receber como parâmetro uma string com o HTML da página de novidades
    Deve fazer o scrape deste HTML para obter a URL da próxima página
    Deve retornar a URL obtida ou None em caso de não haver uma
    """

    soup = BeautifulSoup(html_content, "html.parser")
    anchor = soup.find("a", {"class": "next"})

    if anchor is None:
        return None
    else:
        return anchor.get("href")


def get_url_from_soup(soup):
    "Recupera URL da postagem"
    return soup.find("link", {"rel": "canonical"}).get("href")


def get_title_from_soup(soup):
    "Recupera título da postagem e remove espaços vazios no fim"
    return (soup.find("h1", {"class": "entry-title"}).text).rstrip()


def get_timestamp_from_soup(soup):
    "Recupera data da postagem"
    return soup.find("li", {"class": "meta-date"}).text


def get_writer_from_soup(soup):
    "Recupera autor da postagem"
    author_container = soup.find("span", {"class": "author"})
    return author_container.find("a").text


def get_reading_time_from_soup(soup):
    "Recupera tempo de leiura da postagem e o converte para número inteiro"
    reading_time_text = soup.find("li", {"class": "meta-reading-time"}).text
    reading_time = re.findall(r"\d+", reading_time_text)[0]
    return int(reading_time)


def get_summary_from_soup(soup):
    "Recupera primeiro paragrafo da postagem e remove espaços vazios no fim"
    complete_text = soup.find("div", {"class": "entry-content"})
    summary = complete_text.find("p").text
    return summary.rstrip()


def get_category_from_soup(soup):
    "Recupera categoria da postagem"
    category_container = soup.find("a", {"class": "category-style"})
    return category_container.find("span", {"class": "label"}).text


# Requisito 4
def scrape_news(html_content):
    """
    Deve receber como parâmetro o conteúdo HTML da página de uma única notícia
    Deve um dicionário com os seguintes atributos:
    "url": "https://blog.betrybe.com/novidades/noticia-bacana",
    "title": "Notícia bacana",
    "timestamp": "04/04/2021",
    "writer": "Eu",
    "reading_time": 4,
    "summary": "Algo muito bacana aconteceu",
    "category": "Ferramentas",
    """

    soup = BeautifulSoup(html_content, "html.parser")

    return {
        "url": get_url_from_soup(soup),
        "title": get_title_from_soup(soup),
        "timestamp": get_timestamp_from_soup(soup),
        "writer": get_writer_from_soup(soup),
        "reading_time": get_reading_time_from_soup(soup),
        "summary": get_summary_from_soup(soup),
        "category": get_category_from_soup(soup),
    }


def get_posts_url(amount):
    """
    Retorna uma list de urls de postagens com o tamanho
    igual o valor passado como parametro
    """

    html_content = fetch("https://blog.betrybe.com/")
    fetched_urls = scrape_updates(html_content)
    urls = []
    index = 0

    while len(urls) < amount:
        urls.append(fetched_urls[index])
        index += 1
        if index == len(fetched_urls):
            html_content = fetch(scrape_next_page_link(html_content))
            fetched_urls = scrape_updates(html_content)
            index = 0

    return urls


# Requisito 5
def get_tech_news(amount):
    """
    Recebe um número inteiro N e buscar as últimas N notícias do site
    As notícias buscadas são inseridas no banco de dados
    Após inserir, a função retorna estas mesmas notícias
    """

    posts_url = get_posts_url(int(amount))
    posts_info = [scrape_news(fetch(post)) for post in posts_url]
    create_news(posts_info)

    return posts_info
