# Solicita ao usuário que insira seu nome e armazena a entrada do usuário na variável 'nome'
nome = input("Digite seu nome: ")
# Solicita ao usuário que insira sua idade, converte a entrada do usuário para um inteiro e armazena na variável 'idade'
idade = int(input("Digite sua idade: "))

# Cria uma mensagem personalizada usando a formatação de strings do Python (f-strings)
# A mensagem contém o nome e a idade do usuário
mensagem = f"Olá, {nome}! Você tem {idade} anos."
# Imprime a mensagem personalizada
print(mensagem)