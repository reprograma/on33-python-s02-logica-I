# Este programa exibe informações sobre uma pessoa chamada Jenifer.

# Primeiro, o programa define algumas informações sobre Jenifer.
# "nome" é uma string (uma sequência de caracteres) que contém o nome de Jenifer.
nome = "Jenifer"

# "idade" é um número inteiro que representa a idade de Jenifer.
idade = 33

# "salario" é um número decimal (ou "float") que representa o salário de Jenifer.
salario = 4500.75

# "percentual_aumento" é um número decimal que representa o percentual de aumento no salário de Jenifer.
percentual_aumento = 0.10

# Em seguida, o programa cria uma "f-string", que é uma maneira de formatar strings em Python.
# A f-string contém chaves {} que são substituídas pelos valores das variáveis.
# Por exemplo, {nome} é substituído por "Jenifer", {idade} é substituído por 33, e assim por diante.
# Além disso, :.2f e :.1% são usados para formatar os números decimais.
# :.2f significa "formatar como um número decimal com duas casas decimais".
# :.1% significa "formatar como um percentual com uma casa decimal".
mensagem = f"Nome: {nome}\nIdade: {idade}\nSalário: R${salario:.2f}\nAumento: {percentual_aumento:.1%}"

# Finalmente, o programa exibe a mensagem.
# \n é um caractere especial que cria uma nova linha, então cada parte da mensagem é exibida em uma linha separada.
print(mensagem)

# A saída esperada do programa é:
# Nome: Jenifer
# Idade: 33
# Salário: R$4500.75
# Aumento: 10.0%