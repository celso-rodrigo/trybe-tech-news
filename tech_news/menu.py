import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)


def end_script():
    print("Encerrando script")


def handle_user_input(choosed_option, user_input):
    """Executa função de acordo com escolha e inputs do usuário"""
    cases = {
        0: get_tech_news,
        1: search_by_title,
        2: search_by_date,
        3: search_by_category,
        4: top_5_categories,
        5: end_script,
    }

    function = cases.get(choosed_option)

    if user_input is None:
        return function()
    else:
        return function(user_input)


# Requisitos 11 e 12
def analyzer_menu():
    """
    Responsável pelo menu do nosso programa
    """

    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    responses = [
        "Digite quantas notícias serão buscadas: ",
        "Digite o título: ",
        "Digite a data no formato aaaa-mm-dd: ",
        "Digite a categoria: ",
    ]

    try:
        choosed_option = int(input())
        user_input = None

        if choosed_option in range(4):
            user_input = input(responses[choosed_option])
        elif choosed_option not in range(6):
            raise ValueError()
        return handle_user_input(choosed_option, user_input)
    except ValueError:
        return print("Opção inválida", file=sys.stderr)
