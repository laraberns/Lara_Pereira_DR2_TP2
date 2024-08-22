# README - Tarefas de Programação

## Parte 1: Nível Minhoquinha

### 1. Criação de uma Lista de Caracteres
Crie um programa que receba uma string como entrada do usuário e use um loop `for` para criar uma lista com cada caractere da string.

### 2. Inserção de Números até o Zero
Crie um programa que peça ao usuário para inserir números um de cada vez até que ele digite 0. Armazene esses números em uma lista usando um loop `while`.

### 3. Cálculo da Média dos Valores de uma Lista
Escreva um programa que receba uma lista de números (você pode definir a lista inicialmente, mas certifique-se que o código funcionará para quaisquer listas numéricas) e utilize um loop `for` para calcular a média dos valores da lista.

### 4. Função `imprime_mensagem`
Defina uma função chamada `imprime_mensagem` que receba uma mensagem como argumento e a imprima na tela.

### 5. Função `saudacao`
Crie uma função chamada `saudacao` que imprima uma saudação personalizada, como "Olá, [nome do usuário]!", recebendo o nome como argumento da função.

### 6. Modificação da Função `saudacao`
Usando a mesma implementação da questão 5, modifique a função para que, caso nenhum argumento seja passado, exiba uma saudação genérica.

## Parte 2: Nível Cobrinha

### 1. Função `potencia`
Defina uma função chamada `potencia` que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. A função deve calcular e retornar a base elevada ao expoente.

### 2. Função `maior_valor`
Crie uma função chamada `maior_valor` que receba três números como três argumentos posicionais, exiba o maior número na tela e retorne uma lista ordenada contendo estes números.

### 3. Função `imprime_dados`
Crie uma função chamada `imprime_dados` que receba diversos dados de um produto (nome, preço, quantidade em estoque) como argumentos passados obrigatoriamente por palavras-chave e os imprima de forma organizada.

### 4. DocString
Para cada uma das funções definidas nas questões anteriores, adicione um DocString que explique o propósito da função, seus argumentos e o valor de retorno, se houver, seguindo a folha de estilo exemplificada abaixo.

#### Exemplo de folha de estilo do DocString:

```python
def soma(numero_a, numero_b):
    """
    Realiza a soma entre dois números.

    Args:
    numero_a (int | float): Primeiro número a ser considerado.
    numero_b (int | float): Segundo número a ser considerado.

    Return:
    (int | float): Resultado da soma.
    """
    # Código de implementação da função.
```

### 5. Função `exibir_mensagem`
Defina uma função chamada `exibir_mensagem` que receba um argumento obrigatório `mensagem` e um argumento opcional `repeticoes`, onde `repeticoes` tem um valor padrão de 1. A função deve imprimir a mensagem o número de vezes especificado por `repeticoes`.

### 6. Função `gerar_lista_pares`
Defina uma função chamada `gerar_lista_pares` que receba um número `n`, fornecido pelo usuário, como argumento e retorne uma lista contendo todos os números pares de 0 até `n`. Utilize um laço `for` para preencher a lista.

## Parte 3: Nível Python

### 1. Simulador de Investimentos
Crie um programa que simule o crescimento de um investimento ao longo de um período. O programa deve solicitar ao usuário o valor inicial do investimento, a taxa de juros anual e o número de anos. Em seguida, escreva uma função que calcule o valor final do investimento ao final de cada ano e armazene esses valores em uma lista. Imprima o valor acumulado ano a ano (lembre-se que se trata de juros compostos).

### 2. Cálculo de Consumo de Combustível
Escreva um programa que ajude um motorista a calcular o consumo de combustível de seu veículo. O programa deve solicitar ao usuário que insira a distância percorrida e a quantidade de combustível consumido em várias viagens. Essas informações devem ser armazenadas em uma lista. Em seguida, crie uma função que percorra essa lista e calcule o consumo médio de combustível (km/l) para cada viagem e para o total de todas as viagens.

### 3. Monitoramento de Temperatura
Você foi contratado para desenvolver um software que monitora as temperaturas registradas por sensores em uma fábrica ao longo do dia.

Escreva um programa que utilize um laço `while` para solicitar ao usuário que informe a hora do registro da temperatura (em um número inteiro) seguido do valor da temperatura registrada. Seu programa deverá conter função de validação da entrada do usuário para garantir que a hora descrita esteja entre 0h e 23h e que a temperatura informada esteja entre -15ºC e 60ºC. E em seguida armazene as informações em duas listas, uma com os horários e outra com as temperaturas.

Quando o usuário digitar ‘Fim’, uma função (pode utilizar mais de uma função) deverá receber as duas listas do item anterior como argumentos, calcular a média das temperaturas, ponderada pelo intervalo de tempo entre as medidas e imprimir se a média está dentro do intervalo de segurança (20°C a 30°C) e exibir o horário e o valor da temperatura mais baixa e mais alta do dia.
