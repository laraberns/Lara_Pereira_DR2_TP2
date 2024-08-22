# Quando o usuário digitar ‘Fim’ uma função (pode utilizar mais de uma função) deverá receber as duas listas do item anterior como argumentos, calcular a média das temperaturas, ponderada pelo intervalo de tempo entre as medidas e imprimir se a média está dentro do intervalo de segurança (20°C a 30°C) e exibir o horário e o valor da temperatura mais baixa e mais alta do dia.
lista_horas = []
lista_temperaturas = []

def calcular_registros(lista_horas, lista_temperaturas):
    if not lista_horas or not lista_temperaturas or len(lista_horas) != len(lista_temperaturas):
        print("Dados insuficientes para calcular.")
        return

    intervalo_total = 0
    soma_ponderada = 0
    
    for i in range(1, len(lista_horas)):
        intervalo = lista_horas[i] - lista_horas[i-1]
        intervalo_total += intervalo
        soma_ponderada += intervalo * lista_temperaturas[i]
    
    # Adiciona o primeiro registro, que não tem intervalo anterior
    if len(lista_horas) > 1:
        primeiro_intervalo = lista_horas[1] - lista_horas[0]
        soma_ponderada += primeiro_intervalo * lista_temperaturas[0]
        intervalo_total += primeiro_intervalo

    if intervalo_total == 0:
        media_ponderada = None
    else:
        media_ponderada = soma_ponderada / intervalo_total

    min_temp = max_temp = lista_temperaturas[0]
    hora_min = hora_max = lista_horas[0]
    
    for i in range(1, len(lista_temperaturas)):
        if lista_temperaturas[i] < min_temp:
            min_temp = lista_temperaturas[i]
            hora_min = lista_horas[i]
        if lista_temperaturas[i] > max_temp:
            max_temp = lista_temperaturas[i]
            hora_max = lista_horas[i]

    if media_ponderada is not None:
        if 20 <= media_ponderada <= 30:
            print(f"\nA média ponderada das temperaturas é {media_ponderada:.2f}°C, que está dentro do intervalo de segurança (20°C a 30°C).")
        else:
            print(f"\nA média ponderada das temperaturas é {media_ponderada:.2f}°C, que está fora do intervalo de segurança (20°C a 30°C).")
    else:
        print("Não foi possível calcular a média ponderada.")

    if len(lista_temperaturas) > 0:
        print(f"\nA temperatura mais baixa foi {min_temp:.1f}°C registrada às {hora_min}:00")
        print(f"A temperatura mais alta foi {max_temp:.1f}°C registrada às {hora_max}:00")

while True:
    try:
        hora_registro = int(input("Digite a hora do registro (em número inteiro, 0-23): "))
        
        if hora_registro < 0 or hora_registro > 23:
            print("Erro: Valor da hora digitado errado. Deve ser entre 0h e 23h")
            continue
        
        valor_temperatura = float(input("Digite a temperatura registrada (em ºC): "))

        if valor_temperatura < -15 or valor_temperatura > 60:
            print("Erro: A temperatura está incorreta. Deve ser entre -15ºC e 60ºC")
            continue

        lista_horas.append(hora_registro)
        lista_temperaturas.append(valor_temperatura)
        
        novo_registro = input("Deseja finalizar? Digite 'Fim' para encerrar: ").strip().upper()
        
        if novo_registro == "FIM":
            calcular_registros(lista_horas, lista_temperaturas)
            break
        
    except ValueError:
        print("Por favor, insira um valor válido.")
