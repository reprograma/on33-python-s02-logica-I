def nome_engracado(cor, animal, sobremesa):
    return cor + animal + sobremesa

cor = input("Digite uma cor: ")
animal = input("Digite um animal: ")
sobremesa = input("Digite uma sobremesa: ")

resultado = nome_engracado(cor, animal, sobremesa)
print("O nome engraçado é:", resultado)
