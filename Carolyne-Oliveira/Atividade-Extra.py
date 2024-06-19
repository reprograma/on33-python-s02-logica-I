# Atividade 1: Declare variáveis de diferentes tipos e mostre seus valores e tipos.

# Exemplo de variáveis de diferentes tipos
inteiro = 42
decimal = 3.14
texto = "Olá, mundo!"
booleano = True

# Mostrando os valores e tipos
print(f"inteiro: {inteiro} (tipo: {type(inteiro)})")
print(f"decimal: {decimal} (tipo: {type(decimal)})")
print(f"texto: {texto} (tipo: {type(texto)})")
print(f"booleano: {booleano} (tipo: {type(booleano)})")

# Atividade 2: Receba valores do usuário, faça operações aritméticas e exiba os resultados.

# Recebendo valores do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando operações aritméticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Exibindo os resultados
print(f"Soma: {soma:.2f}")
print(f"Subtração: {subtracao:.2f}")
print(f"Multiplicação: {multiplicacao:.2f}")
print(f"Divisão: {divisao:.2f}")


# Atividade 3: Crie uma função que receba dois números e retorne o maior deles.

def maior_numero(a, b):
    return max(a, b)

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
maior = maior_numero(numero1, numero2)
print(f"O maior número é: {maior:.2f}")

# Atividade 4: Utilize a formatação de strings para criar uma mensagem personalizada.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Criando mensagem personalizada
mensagem = f"Olá, {nome}! Você tem {idade} anos. Bem-vinda ao mundo Python, sua linda!"
print(mensagem)
