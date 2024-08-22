# Defina uma função chamada gerar_lista_pares que receba um número n, fornecido pelo usuário, como argumento e retorne uma lista contendo todos os números pares de 0 até n. Utilize um laço for para preencher a lista.

def gerar_lista_pares(n):
    lista_pares = []
    for i in range(n + 1):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

lista = gerar_lista_pares(4)
print(lista)
