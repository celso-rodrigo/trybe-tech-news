from sys import stderr


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
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a categoria:",
        "Opção inválida",
    ]

    try:
        user_input = int(input())
        if user_input in range(4):
            print(responses[user_input])
        elif user_input not in range(6):
            print("Opção inválida", file=stderr)
    except ValueError:
        return print("Opção inválida", file=stderr)
