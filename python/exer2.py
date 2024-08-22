# Escreva um programa que ajude um motorista a calcular o consumo de combustível de seu veículo. O programa deve solicitar ao usuário que insira a distância percorrida e a quantidade de combustível consumido em várias viagens. Essas informações devem ser armazenadas em uma lista. Em seguida, crie uma função que percorra essa lista e calcule o consumo médio de combustível (km/l) para cada viagem e para o total de todas as viagens.

def calcular_consumo_medio(lista):
    media_viagem = []

    print("\nConsumo de combustível para cada viagem:")
    
    indice_viagem = 0
    for i in lista:
        consumo_viagem = i[0] / i[1]
        media_viagem.append(consumo_viagem)
        indice_viagem += 1
        print(f"O consumo médio da viagem {indice_viagem} foi: {round(consumo_viagem, 2)} km/l")
    
    distancia_total_percorrida = 0
    consumo_total = 0

    for i in lista:
        distancia_total_percorrida += i[0]
        consumo_total += i[1]
    
    media_total = distancia_total_percorrida / consumo_total if consumo_total != 0 else 0
    print(f"\nA distância total percorrida foi: {distancia_total_percorrida} km")
    print(f"O consumo total das viagens foi: {consumo_total} litros")
    print(f"O consumo médio total foi: {round(media_total, 2)} km/l")

lista = []

while True:
    try:
        distancia_percorrida = float(input("Digite a distância percorrida (em km): "))
        quantidade_combustivel_consumido = float(input("Digite a quantidade de combustível consumido (em litros): "))
        
        lista.append([distancia_percorrida, quantidade_combustivel_consumido])
        
        nova_viagem = input("Deseja adicionar nova viagem? S/N: ").strip().upper()
        if nova_viagem != "S":
            break
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

calcular_consumo_medio(lista)

