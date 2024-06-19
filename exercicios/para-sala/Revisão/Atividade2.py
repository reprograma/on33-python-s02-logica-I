# Solicita ao usuário que insira o primeiro número e converte a entrada do usuário para um inteiro
num1 = int(input("Digite o primeiro número: "))
# Solicita ao usuário que insira o segundo número e converte a entrada do usuário para um inteiro
num2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números e armazena o resultado na variável 'soma'
soma = num1 + num2
# Calcula a diferença entre os dois números e armazena o resultado na variável 'diferenca'
diferenca = num1 - num2
# Calcula o produto dos dois números e armazena o resultado na variável 'produto'
produto = num1 * num2
# Calcula a divisão do primeiro número pelo segundo e armazena o resultado na variável 'divisao'
divisao = num1 / num2

# Imprime a soma dos dois números
print(f"Soma: {soma}")
# Imprime a diferença entre os dois números
print(f"Diferença: {diferenca}")
# Imprime o produto dos dois números
print(f"Produto: {produto}")
# Imprime a divisão do primeiro número pelo segundo
print(f"Divisão: {divisao}")