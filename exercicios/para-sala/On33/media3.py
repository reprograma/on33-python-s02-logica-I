def calcular_media_ponderada(nota1, peso1, nota2, peso2):
    # Calcular a média ponderada
    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

# Exemplo de uso da função
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

media_calculada = calcular_media_ponderada(nota1, peso1, nota2, peso2)
print(f"A média ponderada das notas é: {media_calculada}")

def calcular_recuperacao(nota_regular, nota_recuperacao):
    # Calcular a nota de recuperação
    media = (nota_regular + nota_recuperacao) / 2

# Exemplo de uso da função
nota_regular = float(input("Digite a nota regular: "))
nota_recuperacao = float(input("Digite a nota de recuperação: "))

recuperacao_calculada = calcular_recuperacao(nota_regular, nota_recuperacao)
print(f"A nota de recuperação é: {recuperacao_calculada}")

