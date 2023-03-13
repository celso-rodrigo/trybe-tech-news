from tech_news.database import search_news
import re


# Requisito 7
def search_by_title(title):
    """
    Deve receber uma string com um título de notícia
    Deve buscar as notícias do banco de dados por título
    Deve retornar uma lista de tuplas com as notícias encontradas nesta busca
    """

    pattern = re.compile(rf"{title}", re.IGNORECASE)
    news = search_news({"title": {"$regex": pattern}})

    return [
        (new["title"], new["url"])
        for new in news
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
