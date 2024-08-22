# Crie um programa que peça ao usuário para inserir números um de cada vez até que ele digite 0. Armazene esses números em uma lista usando um loop while.

numero_digitado = int(input("Digite um número: "))
lista = []

while (numero_digitado != 0):
    lista.append(numero_digitado)
    numero_digitado = int(input("Digite um número: "))
     
else:
      print("Você digitou zero!")

print(lista)