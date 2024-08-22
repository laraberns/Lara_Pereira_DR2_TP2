# Escreva um programa que utilize um laço while para solicitar ao usuário que informe a hora do registro da temperatura (em um número inteiro) seguido do valor da temperatura registrada. Seu programa deverá conter função de validação da entrada do usuário para garantir que a hora descrita esteja entre 0h e 23h e que a temperatura informada esteja entre -15ºC e 60ºC. E em seguida armazene as informações em duas listas, uma com os horários e outra com as temperaturas.

lista_horas = []
lista_temperaturas = []

while True:
    try:
        hora_registro = int(input("Digite a hora do registro (Em número inteiro. Ex: 8)): "))
        
        if hora_registro < 0 or hora_registro > 23:
            print("Erro: Valor da hora digitado errado. Deve ser entre 0h e 23h")
            continue  
        
        valor_temperatura = float(input("Digite a temperatura registrada: "))

        if valor_temperatura < -15 or valor_temperatura > 60:
            print("Erro: A temperatura está incorreta. Deve ser entre -15 e 60")
            continue  

        lista_horas.append(hora_registro)
        lista_temperaturas.append(valor_temperatura)
        
        novo_registro = input("Deseja adicionar novo registro? S/N: ").strip().upper()
        
        if novo_registro != "S":
            break
        
    except ValueError:
        print("Por favor, insira um valor válido.")