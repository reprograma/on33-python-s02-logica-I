# Definição da função 'maior_numero' que recebe dois argumentos: a e b
def maior_numero(a, b):
    # Retorna o maior valor entre a e b usando a função 'max' do Python
    return max(a, b)

# Solicita ao usuário que insira o primeiro número e converte a entrada do usuário para um float
num1 = float(input("Digite o primeiro número: "))
# Solicita ao usuário que insira o segundo número e converte a entrada do usuário para um float
num2 = float(input("Digite o segundo número: "))

# Imprime o maior número entre num1 e num2, chamando a função 'maior_numero' com num1 e num2 como argumentos
print(f"O maior número é: {maior_numero(num1, num2)}")