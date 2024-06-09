##### Operadores Aritméticos #####
# Adição
resultado = 5 + 3  # Resultado será 8

# Subtração
resultado = 10 - 4  # Resultado será 6

# Multiplicação
resultado = 3 * 4  # Resultado será 12

# Divisão
resultado = 20 / 5  # Resultado será 4.0 (em Python 3, a divisão retorna um float)

# Divisão Inteira
resultado = 20 // 6  # Resultado será 3 (a parte decimal é descartada)

# Módulo (Resto da Divisão)
resultado = 20 % 6  # Resultado será 2 (20 dividido por 6 tem resto 2)

# Exponenciação
resultado = 2 ** 3  # Resultado será 8 (2 elevado à potência de 3)


##### Operadores Atribuição #####
# Atribuição Simples
x = 10  # A variável x recebe o valor 10

# Atribuição com Operação
x += 5  # Equivalente a x = x + 5 (x será 15)
y -= 3  # Equivalente a y = y - 3 (y deve ter um valor previamente definido)

# Atribuição com Expressão
x = (x + 5) * 2  # Equivalente a x = (x + 5) * 2 (x deve ter um valor previamente definido)     

##### Operadores de Comparação #####

x = 10
y = 5

# Igual a
resultado = x == y  # False, porque 10 não é igual a 5

# Diferente de
resultado = x != y  # True, porque 10 é diferente de 5

# Menor que
resultado = x < y  # False, porque 10 não é menor que 5

# Maior que
resultado = x > y  # True, porque 10 é maior que 5

# Menor ou igual a
resultado = x <= y  # False, porque 10 não é menor ou igual a 5

# Maior ou igual a
resultado = x >= y  # True, porque 10 é maior ou igual a 5

#### Operadores Lógicos ####
x = True
y = False

# E Lógico
resultado = x and y  # False, porque True e False é False

# Ou Lógico
resultado = x or y  # True, porque True ou False é True

# Não Lógico
resultado = not x  # False, porque não True é False

#### Operadores de Pertencimento ####

frutas = ["maçã", "banana", "cereja"]

# Está em
resultado = "banana" in frutas  # True, porque "banana" está na lista de frutas

# Não está em
resultado = "uva" not in frutas  # True, porque "uva" não está na lista de frutas

#### Operadores de Identidade ####

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# É
resultado = x is z  # True, porque x e z referenciam o mesmo objeto na memória

# Não é
resultado = x is not y  # True, porque x e y referenciam objetos diferentes na memória

