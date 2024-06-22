nome2 = int(input("Olá, gostaria de saber seu nome de gamer? Insira a sua data de nascimento: "))
nome1 = int(input("Agora insira o seu mês de nascimento (número de 1 a 12): "))
nome3 = int(input("Por fim, insira o último número do seu ano de nascimento: "))

def gerador_de_nomes():
    global nome1, nome2, nome3

    if nome1 ==  1 or nome1 == 2 or nome1 == 3:
      nome1 = "Serpente"
    elif nome1 ==  4 or nome1 == 5 or nome1 == 6:
      nome1 = "Fênix"
    elif  nome1 ==  7 or nome1 == 8 or nome1 == 9:
      nome1 = "Zumbi"
    elif nome1 ==  10 or nome1 == 11 or nome1 == 12:
      nome1 = "Fantasma"

    if nome2 == 1 or nome2 == 2 or nome2 == 3 or nome2 == 4 or nome2 == 5:
      nome2 = "Mutante"
    elif nome2 == 6 or nome2 == 7 or nome2 == 8 or nome2 == 9 or nome2 == 10:
      nome2 = "Invencível"
    elif nome2 == 11 or nome2 == 12 or nome2 == 13 or nome2 == 14 or nome2 == 15:
      nome2 = "Invisível"
    elif nome2 == 16 or nome2 == 17 or nome2 == 18 or nome2 == 19 or nome2 == 20:
      nome2 = "Líder"
    elif nome2 == 21 or nome2 == 22 or nome2 == 23 or nome2 == 24 or nome2 == 25:
      nome2 = "Noob"
    elif nome2 == 26 or nome2 == 27 or nome2 == 28 or nome2 == 29 or nome2 == 30 or nome2 == 31:
      nome2 = "Hacker"

    if nome3 ==  0 or nome3 ==  1 or nome3 == 2 or nome3 == 3:
      nome3 = "Biruta"
    elif nome1 ==  4 or nome3 == 5 or nome3 == 6:
      nome3 = "Tiltado"
    elif  nome3 ==  7 or nome3 == 8 or nome3 == 9:
      nome3 = "Overpower"

    return nome1, nome2, nome3

nome1_gerado, nome2_gerado, nome3_gerado = gerador_de_nomes()
print("Parabéns! Seu nome gamer é: " + nome1_gerado, nome2_gerado, nome3_gerado)