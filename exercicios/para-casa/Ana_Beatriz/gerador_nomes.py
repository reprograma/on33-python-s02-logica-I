cor = input("Digite sua cor favorita: ")
animal = input("Difgite um animal de sua preferencia: ")
sobremesa = input("Digite a sobremesa que mais gosta: ")


print(f"SEU NOME DIVERTIDO É: " + cor.upper(), animal.upper(), sobremesa.upper())

#aproveitando o dia dos namorados, vamos ser criativos

valor1 = int(input("Digite um numero:"))
valor2 = int(input("Digite outro numero:"))

lista1 =[3,9,5,7,0]
lista2 =[1,8,40,78]

if valor1 in lista1 and valor2 in lista2:
  print(f"te amo")
  print(f"feliz dia dos namorados")
elif valor1 in lista1 or valor2 in lista2:
  print(f"te amo")
else:
    print(f"você errou")  