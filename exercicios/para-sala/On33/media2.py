# Definição da função 'media' que recebe dois argumentos: nota1 e nota2
def media(nota1, nota2):
    # Calcula a média das duas notas e armazena o resultado na variável 'resultadoMedia'
    resultadoMedia = (nota1 + nota2) / 2
    # Imprime a primeira nota
    print('Nota 1:', nota1)
    # Imprime a segunda nota
    print('Nota 2:', nota2)
    # Imprime a média das notas
    print('A Média das notas é:', resultadoMedia)

# Define a variável 'nota1' com o valor 8
nota1 = 8
# Define a variável 'nota2' com o valor 9
nota2 = 9
# Chama a função 'media' passando 'nota1' e 'nota2' como argumentos
media(nota1, nota2)