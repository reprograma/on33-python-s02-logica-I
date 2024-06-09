# Este programa define uma função para calcular a média de quatro notas e, em seguida, usa essa função para calcular uma média.

# Primeiro, o programa define uma função chamada "calcular_media".
# A função recebe quatro argumentos: nota1, nota2, nota3 e nota4.
def calcular_media(nota1, nota2, nota3, nota4):
    # Dentro da função, o programa calcula a soma das quatro notas.
    soma = nota1 + nota2 + nota3 + nota4  # Operador de adição
    
    # Em seguida, divide a soma pelo número de notas (4) para obter a média.
    media = soma / 4  # Operador de divisão
    
    # A função retorna o valor da média.
    return media

# Depois de definir a função, o programa a usa para calcular a média de quatro notas: 8.5, 7.0, 9.5 e 6.0.
media = calcular_media(8.5, 7.0, 9.5, 6.0)

# O programa exibe a média calculada.
print(f"A média das notas é: {media}")  # Saída: A média das notas é: 7.75

# O programa também mostra como você pode chamar a função com argumentos nomeados.
# Com argumentos nomeados, você pode passar os argumentos fora da ordem em que foram definidos na função.
# Por exemplo, você pode passar nota3 antes de nota1.
media = calcular_media(nota3=9.5, nota1=8.5, nota4=6.0, nota2=7.0)

# O programa exibe a média calculada.
print(f"A média das notas é: {media}")  # Saída: A média das notas é: 7.75