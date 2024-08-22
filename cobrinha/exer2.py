# Crie uma função chamada maior_valor que receba três números como trê argumentos posicionais, exiba o maior número na tela e retorne uma lista ordenada contendo estes números.

def maior_valor(num1, num2, num3):
    """
    Recebe três números e imprime na tela o maior número recebido e retorna uma lista ordenada dos números.
    
    Args:
    num1 (int float): Um Número
    num2 (int float): Um Número
    num3 (int float): Um Número

    Retorna:
    list: Lista crescente dos números recebidos
    """
    maior = max(num1, num2, num3)
    print(maior)
    return sorted([num1, num2, num3])

resultado = maior_valor(3, 1, 2)
print("Lista ordenada:", resultado)