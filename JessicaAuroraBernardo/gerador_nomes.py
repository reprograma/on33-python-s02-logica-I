# Gerador de nomes divertidos versão DRAG QUEEN

# Dicionário para os meses e seus nomes
meses = {'1': 'Lady',
    '2': 'Mistres',
    '3': 'Madame',
    '4': 'Candy',
    '5': 'Roxy',
    '6': 'Miss',
    '7': 'Divine',
    '8': 'Acid',
    '9': 'Trinity',
    '10': 'Alyssa',
    '11': 'Violet',
    '12': 'Scarlet'}

# Dicionário para os dias e seus sobrenomes
dias = {'1': 'Love Hot',
    '2': 'Spacate Alert',
    '3': 'Delicius Fox',
    '4': 'Von Hunty',
    '5': 'Plstique Tiara',
    '6': 'Big Boogie',
    '7': 'Sugar Candy',
    '8': 'Essence Hall',
    '9': 'Del Rio',
    '10': 'Willow Pill',
    '11': 'Love Hot',
    '12': 'Spacate Alert',
    '13': 'Delicius Fox',
    '14': 'Von Hunty',
    '15': 'Plstique Tiara',
    '16': 'Big Boogie',
    '17': 'Sugar Candy',
    '18': 'Essence Hall',
    '19': 'Del Rio',
    '20': 'Willow Pill',
    '21': 'Love Hot',
    '22': 'Spacate Alert',
    '23': 'Delicius Fox',
    '24': 'Von Hunty',
    '25': 'Plstique Tiara',
    '26': 'Big Boogie',
    '27': 'Sugar Candy',
    '28': 'Essence Hall',
    '29': 'Del Rio',
    '30': 'Willow Pill',
    '31': 'Chocolate Milk'}

# Definição das 3 variáveis solicitadas
mes = input("Digite o mês do seu aniversário (por exemplo, 1 para janeiro, 2 para fevereiro, etc.): ")
dia = input("Digite o dia do seu aniversário: ")
sobrenome = input("Digite um sobrenome bem brasileiro: ")

# Combinação dos nomes
nome_drag = meses[mes] + ' ' + dias[dia] + ' ' + sobrenome

# Resposta
print(f'Seu nome brasileirissímo de Drag é: {nome_drag}')

