# primeiro eu criei uma função chamada 'nome_engracado' que recebe os três nomes que a professora solicitou: cor, animal e sobremesa.
# depois eu usei as funções pra juntar as palavras em uma única string.
def nome_engracado(cor, animal, sobremesa):
    return cor + animal + sobremesa

# daí o input pede pro usuário digitar uma cor, um animal e uma sobremesa
cor = input("Digite uma cor: ")
animal = input("Digite um animal: ")
sobremesa = input("Digite uma sobremesa: ")

# daí criei um comando pra chamar 'nome_engracado' com as variáveis 'cor', 'animal' e 'sobremesa' 
# e juntar tudo na nova variável resultado
resultado = nome_engracado(cor, animal, sobremesa)

# daí pedi pro programa exibir o resultado na tela
print("O nome engraçado é:", resultado)
