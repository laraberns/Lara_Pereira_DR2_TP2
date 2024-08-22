valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual sem o % (Ex: 10): "))
numero_anos = int(input("Digite o número de anos: "))

def calcular_valor_final(valor_inicial, taxa_juros_anual, numero_anos):
    taxa_juros_anual = taxa_juros_anual / 100
    lista_valor_final_ano = []

    for ano in range(1, numero_anos + 1):
        valor_final = valor_inicial * (1 + taxa_juros_anual) ** ano
        lista_valor_final_ano.append(round(valor_final, 2))
    
    return lista_valor_final_ano

lista_valores = calcular_valor_final(valor_inicial, taxa_juros_anual, numero_anos)

print("Valor acumulado ao final de cada ano:")
for ano, valor in enumerate(lista_valores, start=1):
    print(f"Ano {ano}: R$ {valor:.2f}")
