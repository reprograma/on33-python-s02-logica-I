dia_nascimento = int(input('Insira o dia do seu nascimento no formato DD: '))
mes_nascimento = int(input('Insira o mês do seu nascimento no formato MM: '))
ano_nascimento = int(input('Digite seu ano de nascimento: '))

def calcular_animal_zodiaco_chines(ano):
    animais_zodiaco = ['Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente',
                    'Cavalo', 'Carneiro', 'Macaco', 'Galo', 'Cão', 'Porco']
    indice = (ano - 1924) % 12
    return animais_zodiaco[indice]   

def calcular_elemento_zodiaco_chines(ano):
    elementos_zodiaco = ['Metal', 'Àgua', 'Madeira', 'Fogo', 'Terra']
    return elementos_zodiaco[(ano % 10) // 2]

def calcular_estacao_nascimento_zodiaco_chines(dia, mes):
    if (mes == 2 and dia >= 4) or (mes == 5 and dia <= 5) or (2 < mes < 5):
        return 'Primaveril' 
    
    elif (mes == 5 and dia >= 6) or (mes == 8 and dia <= 6) or (5 < mes < 8):
        return 'Veranil'
    
    elif (mes == 8 and dia >= 7) or (mes == 11 and dia <= 6) or (8 < mes < 11):
        return 'Outonal'

    else:
        return 'Inverno'



animal = calcular_animal_zodiaco_chines(ano_nascimento)
elemento = calcular_elemento_zodiaco_chines(ano_nascimento)
estacao = calcular_estacao_nascimento_zodiaco_chines(dia_nascimento, mes_nascimento)


print(f'O seu nome celestial baseado no Horóscopo chinês é: {animal} de {elemento} {estacao}.')
