from tech_news.database import search_news
from datetime import datetime
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

    return [(new["title"], new["url"]) for new in news]


def validate_date(date):
    """
    Recebe um data e retorna
    True caso o formato seja YYYY-MM-DD
    False em qualquer outro caso
    """

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Requisito 8
def search_by_date(date):
    """
    Deve receber como parâmetro uma data no formato AAAA-mm-dd
    Deve buscar as notícias do banco de dados por data
    Deve retornar uma lista de tuplas com as notícias encontradas nesta busca
    Caso a data seja inválida, lança uma exceção ValueError("Data inválida")
    """

    if not validate_date(date):
        raise ValueError("Data inválida")
    else:
        timestamp = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = search_news({"timestamp": timestamp})

        return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
