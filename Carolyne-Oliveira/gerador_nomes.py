#- Implemente o programa que gera nomes divertidos combinando palavras das categorias fornecidas: cores, animais e sobremesas.
#- Utilize entradas do usuário para obter as palavras e combine-as de maneira criativa.

# Início do Gerador de Nomes Engraçados
inicio = input("Olá, vamos começar? (sim/não): ")

# Verifica a resposta do usuário
if inicio.lower() == "sim":
    # Solicita ao usuário para inserir uma cor
    cor = input("Primeiro digite uma cor: ")

    # Solicita ao usuário para inserir um animal
    animal = input("Depois digite um animal: ")

    # Solicita ao usuário para inserir uma sobremesa
    sobremesa = input("E por último digite uma sobremesa: ")

    # Combina as palavras em uma frase divertida
    frase_divertida = f"Seu nome divertido é {animal} {cor} {sobremesa}."
    print(frase_divertida)
# Mensagem se o usuário não quiser continuar e tiver digitado ‘não’ no início     
else:
    print("Poxa, que pena!")
