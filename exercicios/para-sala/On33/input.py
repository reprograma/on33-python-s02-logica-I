# Este programa pede ao usuário para digitar seu nome e, em seguida, exibe uma saudação personalizada.

# Primeiro, o programa usa a função "input" para pedir ao usuário para digitar seu nome.
# A função "input" exibe o texto entre parênteses (neste caso, "Digite seu nome: ") e, em seguida, espera o usuário digitar algo.
# O que o usuário digitar será armazenado na variável "nome".
nome = input("Digite seu nome: ")

# Em seguida, o programa usa a função "print" para exibir uma saudação personalizada.
# A função "print" exibe o texto entre parênteses na tela.
# Neste caso, o texto é "Olá, " seguido pelo nome que o usuário digitou.
# Por exemplo, se o usuário digitou "Maria", o programa exibirá "Olá, Maria".
print("Olá,", nome)