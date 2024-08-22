# Crie uma função chamada imprime_dados que recebe diversos dados de um produto (nome, preço, quantidade em estoque) como argumentos passados obrigatoriamente por palavras-chave e os imprima de forma organizada.

def imprime_dados(*,nome, preco, quantidade):
    """
    Recebe dados diversos de um produto e imprime na tela de forma estruturada.
    
    Args:
    nome (str): Nome do produto
    preco (int float): Preço do produto
    quantidade (int): Quantidade em estoque

    Retorna:
    A função não retorna nenhum valor. Apenas imprime as informações.
    """
    print(f"O produto {nome} custa {preco} e possui {quantidade} de quantidade.")

imprime_dados(nome="Caderno", preco=29.90, quantidade=100)