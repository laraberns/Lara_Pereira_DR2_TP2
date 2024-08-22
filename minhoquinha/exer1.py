# Crie um programa que receba uma string como entrada do usuário e use um loop for para criar uma lista com cada caractere da string.

entrada = input("Digite uma palavra: ")
lista = []

for char in entrada:
    lista.append(char)

print(lista)