from tech_news.database import find_news


def get_category_ocorrencias():
    """
    Busca categorias no banco de dados e calcula o número de ocorrências
    Exemplo de retorno:
    [{"categoria_um": 3, "categoria_dois": 1, "categoria_tres": 2}]
    """

    news = find_news()
    categories = {}

    for new in news:
        category = new["category"]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    return categories


# Requisito 10
def top_5_categories():
    """
    Retorna lista com 5 categorias mais comuns no banco de dados
    Categorias são ordenadas de forma decrescente e alfabética
    """

    categories = get_category_ocorrencias()
    ordered_categories = dict(
        sorted(categories.items(), key=lambda item: (-item[1], item[0]))
    )

    return list(ordered_categories.keys())[:5]
