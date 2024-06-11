# Exercicio - Método 1:

cor = str(input('Informe uma cor: '))
animal = str(input('Informe um animal: '))
sobremesa = str(input('Informe um sobremesa: '))

nome_divertido = cor, animal, sobremesa

print('Seu nome divertido é', cor, animal, sobremesa)

print('======================================================')
# Exercicio - Método 2 - Utilizando função:

def gerar_nome_divertido():
    cor = str(input('Informe uma cor: '))
    animal = str(input('Informe um animal: '))
    sobremesa = str(input('Informe uma sobremesa: '))

    nome_divertido = f"{cor} {animal} {sobremesa}"
    
    print('Seu nome divertido é', nome_divertido)

gerar_nome_divertido()

print('======================================================')

# Exercicio - Método 3 - Utilizando random:

import random

cores = ['Vermelho', 'Verde', 'Azul','Rosa','Marron','Amarelo','Roxo','Laranja','Verde Lesbico', 'Arco-Iris']
animais = ['Cachorra','Gata','Elefante','Calopsita','Leoa','Cobra','Macaco','Zebra','Baleia','Cavala']
sobremesa = ['Bolo', 'Torta de Limão','Torta de Bolacha','Pudim','Sorvete','Quindim','Alfajor','Marshmallow','Bombom','Rocambole']

cor = random.choice(cores)
animal = random.choice(animais)
sobremesa = random.choice(sobremesa)

nome_divertido = f"{cor} {animal} {sobremesa}"

print('Seu nome divertido é', nome_divertido)