# Defina uma função chamada potencia que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. A função deve calcular e retornar a base elevada ao expoente.

def potencia(base,expoente = 2):
    """
    Recebe dois números, sendo um base e outro expoente e calcula a potência.
    
    Args:
    base (int float): Número base
    expoente (int float): Número expoente. Possui como padrão o 2

    Retorna:
    (int float): Resultado da exponenciação.
    """
    return base ** expoente

resultado = potencia(2,2)

print(resultado)