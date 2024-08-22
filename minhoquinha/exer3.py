# Escreva um programa que receba uma lista de números (você pode definir a lista inicialmente, mas certifique-se que o código funcionará para quaisquer listas numéricas) e utilize um loop for para calcular a média dos valores da lista.

numeros = [1,2,3,4,5]
soma = 0

for char in numeros:
    soma += char

media = soma / len(numeros)

print("A média dos valores da lista é:", round(media, 2))

