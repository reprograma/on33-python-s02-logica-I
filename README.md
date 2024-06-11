EXERCICIO DA AULA DA SEMANA 02
**# Introdução**
Foi demandado que criassemos um programa gerador de nomes aleatório com base nas respostas do usuário.
As respostas seriam referentes as seguintes perguntas:
1. Qual sua cor favorita?
2. Qual animal te representa mais?
3. Qual sua sobremesa favorita?
**# Resolução**
Criei um input() para cada pergunta:

Cor = input('Qual sua cor favorita? ')
Animal = input('Qual animal te representa mais? ')
Sobremesa = input('Qual sua sobremesa favorita? ')

E para finalmente gerar o nome divertido para o usuário, criei um print() que chamasse as três variáveis criadas acima:

print(f'Seu nome divertido é {Animal} {Cor} {Sobremesa}!')