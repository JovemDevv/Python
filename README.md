# Python

estudos e praticas

## ENTRADA E SÁIDA DE DADOS

(f'asdsa {sdasd}') format string: para colocar uma variavel na string. minha estring será criada a partir de alguma coisa dinamica, pode mudar.

input()   = entrada de algum dado para alguma variavel. espera alguma reposta.

print()


## CONVERSÃO DE DADOS

Conversão de dados (ou casting) em Python significa transformar um tipo de dado em outro. Isso é útil quando queremos operar valores de tipos diferentes juntos.
Principais conversões:

    int() → Converte para número inteiro
    float() → Converte para número decimal
    str() → Converte para texto (string)
    bool() → Converte para verdadeiro (True) ou falso (False)


## OPERADORES ARITMETICOS

Os operadores aritméticos são usados para realizar cálculos matemáticos em programação. Eles são essenciais para manipular números em qualquer linguagem de programação. Vamos ver os principais operadores aritméticos:

Em Python, os operadores aritméticos funcionam da mesma maneira que em outras linguagens de programação, mas com a sintaxe própria da linguagem. Vamos ver como usá-los com exemplos:

1. **Soma (+)**:
   Adiciona dois números.
   ```python
   a = 5
   b = 3
   resultado = a + b
   print(resultado)  # Saída: 8
   ```

2. **Subtração (-)**:
   Subtrai um número de outro.
   ```python
   a = 7
   b = 2
   resultado = a - b
   print(resultado)  # Saída: 5
   ```

3. **Multiplicação (*)**:
   Multiplica dois números.
   ```python
   a = 4
   b = 3
   resultado = a * b
   print(resultado)  # Saída: 12
   ```

4. **Divisão (/) e divisão inteira (//)**:
   - A divisão normal (`/`) retorna um número decimal.
   - A divisão inteira (`//`) retorna o resultado da divisão sem a parte decimal (apenas a parte inteira).
   
   ```python
   a = 10
   b = 3
   resultado_divisao = a / b
   print(resultado_divisao)  # Saída: 3.3333333333333335
   
   resultado_divisao_inteira = a // b
   print(resultado_divisao_inteira)  # Saída: 3
   ```

5. **Módulo (%)**:
   Retorna o **resto** da divisão entre dois números.
   ```python
   a = 10
   b = 3
   resultado_modulo = a % b
   print(resultado_modulo)  # Saída: 1
   ```

6. **Exponenciação (**) ou Potência**:
   Eleva um número a uma potência.
   ```python
   a = 2
   b = 3
   resultado_potencia = a ** b
   print(resultado_potencia)  # Saída: 8
   ```

## OPERADORES RELACIONAIS

Operadores relacionais em lógica de programação, como no Python, são usados para comparar dois valores. Eles retornam **True** (verdadeiro) ou **False** (falso), dependendo do resultado da comparação. São úteis para tomar decisões em um programa, como em estruturas condicionais (if, while, etc.).

Aqui estão os operadores relacionais mais comuns:

1. **`==`** (igual a): Verifica se dois valores são iguais.
   - Exemplo: `5 == 5` retorna **True**.

2. **`!=`** (diferente de): Verifica se dois valores são diferentes.
   - Exemplo: `5 != 3` retorna **True**.

3. **`>`** (maior que): Verifica se o valor da esquerda é maior que o da direita.
   - Exemplo: `7 > 5` retorna **True**.

4. **`<`** (menor que): Verifica se o valor da esquerda é menor que o da direita.
   - Exemplo: `3 < 5` retorna **True**.

5. **`>=`** (maior ou igual a): Verifica se o valor da esquerda é maior ou igual ao da direita.
   - Exemplo: `5 >= 5` retorna **True**.

6. **`<=`** (menor ou igual a): Verifica se o valor da esquerda é menor ou igual ao da direita.
   - Exemplo: `4 <= 5` retorna **True**.

Esses operadores são essenciais para fazer comparações e controlar o fluxo do seu programa com base em condições.

## OPERADORES LOGICOS

Os operadores lógicos em programação são usados para combinar expressões booleanas (que podem ser **True** ou **False**). Eles permitem criar condições mais complexas para controlar o fluxo de um programa. No Python, os operadores lógicos são os seguintes:

1. **`and`** (e): Retorna **True** se **todas** as expressões forem verdadeiras. Se alguma for **False**, o resultado será **False**.
   - Exemplo: 
     ```python
     True and False  # Retorna False
     True and True   # Retorna True
     ```

2. **`or`** (ou): Retorna **True** se **pelo menos uma** das expressões for verdadeira. Só retorna **False** se **todas** as expressões forem falsas.
   - Exemplo: 
     ```python
     False or True   # Retorna True
     False or False  # Retorna False
     ```

3. **`not`** (não): Inverte o valor lógico de uma expressão. Se a expressão for **True**, o `not` retorna **False**, e se for **False**, ele retorna **True**.
   - Exemplo: 
     ```python
     not True  # Retorna False
     not False # Retorna True
     ```

### Exemplos de uso em Python:

```python
a = 5
b = 10

# Usando 'and'
if a > 0 and b > 0:
    print("Ambos os números são positivos")

# Usando 'or'
if a < 0 or b > 0:
    print("Pelo menos um número é negativo")

# Usando 'not'
if not(a < 0):
    print("O número 'a' não é negativo")
```

Esses operadores lógicos são muito úteis quando você precisa combinar várias condições dentro de estruturas de controle, como **if** e **while**.

## ESTRUTURAS DE DECISÃO

Estruturas de decisão são usadas em programação para controlar o fluxo do programa com base em condições. Elas permitem que o programa tome diferentes caminhos, dependendo do que é verdadeiro ou falso em uma condição. No Python, as principais estruturas de decisão são:

### 1. **`if`** (se)

A estrutura **`if`** executa um bloco de código **se** a condição for verdadeira.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

### 2. **`if-else`** (se... senão)

A estrutura **`if-else`** permite que você execute um bloco de código **se** a condição for verdadeira, e outro bloco de código **senão**.

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### 3. **`if-elif-else`** (se... senão se... senão)

A estrutura **`if-elif-else`** é usada quando você tem várias condições para verificar. O programa verificará cada condição na ordem e executará o bloco de código correspondente à primeira condição verdadeira.

```python
nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")
```

### 4. **`if` dentro de `if`** (Estruturas aninhadas)

Você pode ter **`if`** dentro de outros **`if`**, o que cria uma decisão mais complexa.

```python
idade = 20
tem_habilitacao = True

if idade >= 18:
    if tem_habilitacao:
        print("Você pode dirigir.")
    else:
        print("Você precisa de habilitação para dirigir.")
else:
    print("Você é menor de idade.")
```

### Resumo:

- **`if`**: Executa um bloco de código se a condição for verdadeira.
- **`if-else`**: Executa um bloco de código se a condição for verdadeira, e outro se for falsa.
- **`if-elif-else`**: Verifica múltiplas condições em sequência.
- **`if` aninhado**: Um **`if`** dentro de outro para verificações mais detalhadas.

Essas estruturas são fundamentais para a lógica de programação e ajudam a criar programas dinâmicos, que se comportam de maneiras diferentes dependendo das entradas ou condições que o programa encontra.

Ex:
idade = int(input("Digite a sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

exercicio:
``` # Recebe uma temperatura em Fahrenheit e exibe em graus Celsius.

temperatura_farenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Converte para Celsius
temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

# Exibe o valor convertido com 2 casas decimais
print(f"Convertida ficou em: {temperatura_celsius:.2f}°C")

A parte {temperatura_celsius:.2f} faz com que o valor de temperatura_celsius seja exibido com 2 casas decimais. ```

