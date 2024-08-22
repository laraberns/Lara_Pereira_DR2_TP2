# Defina uma função chamada exibir_mensagem que receba um argumento obrigatório mensagem e um argumento opcional repeticoes, onde repeticoes tem um valor padrão de 1. A função deve imprimir a mensagem o número de vezes especificado por repeticoes.

def exibir_mensagem(mensagem, repeticoes = 1):
    for num in range (repeticoes):
        print(mensagem)

exibir_mensagem("Meu nome é Lara", 2)
exibir_mensagem("Meu nome é Pedro")