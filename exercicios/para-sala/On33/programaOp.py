# Este programa realiza várias operações com dois números digitados pelo usuário.

# Primeiro, o programa pede ao usuário para digitar dois números.
# A função "input" exibe o texto entre parênteses e, em seguida, espera o usuário digitar algo.
# O que o usuário digitar será convertido para um número inteiro pela função "int" e armazenado nas variáveis "num1" e "num2".
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:'))

# Em seguida, o programa realiza várias operações aritméticas com os números e armazena os resultados em variáveis.
soma = num1 + num2  # Soma
subtracao = num1 - num2  # Subtração
multiplicacao = num1 * num2  # Multiplicação
divisao = num1 / num2  # Divisão
divisaoInteira = num1 // num2  # Divisão inteira
modulo = num1 % num2  # Módulo (resto da divisão)
potencia = num1 ** num2  # Potência

# O programa exibe os resultados das operações aritméticas.
print('\n Resultados das operações aritmeticas:')
print('Soma:', soma)
print('Subtracao:', subtracao)
print('Multiplicacao:', multiplicacao)
print('Divisao:', divisao)
print('DivisaoInteira:', divisaoInteira)
print('Modulo:', modulo)
print('Potencia:', potencia)

# O programa realiza várias comparações com os números e exibe os resultados.
print('\n Resultados das operações de comparação:')
print('Igualdade:', num1 == num2)  # Igualdade
print('Diferenca:', num1 != num2)  # Diferença
print('Maior:', num1 > num2)  # Maior
print('Maior ou igual:', num1 >= num2)  # Maior ou igual
print('Menor:', num1 < num2)  # Menor
print('Menor ou igual:', num1 <= num2)  # Menor ou igual

# O programa realiza algumas operações de atribuição e exibe os resultados.
print('\n Resultados dos Operadores de atribuição:')
num1 += 5  # Adiciona 5 a num1
print('num1 += 5:', num1)
num2 /= 2  # Divide num2 por 2
print('num2 /= 2:', num2)

# O programa verifica se num1 está em uma lista de números e exibe o resultado.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f'o número {num1} está na lista de numeros')
else:
    print(f'o número {num1} não está na lista de números')

# O programa compara a identidade de alguns objetos e exibe os resultados.
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('\n Resultados das operações de identidade de objetos:')
print('x is z:', x is z)  # x é o mesmo objeto que z
print('x is y:', x is y)  # x não é o mesmo objeto que y
print('x is not y:', x is not y)  # x não é o mesmo objeto que y