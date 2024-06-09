# Este programa coleta informações sobre uma aluna e as exibe.

# Primeiro, o programa pede ao usuário para inserir o nome da aluna.
nome = input("Digite o nome da aluna: ")

# Em seguida, pede a idade da aluna. Como a idade é um número, ela é convertida para um número inteiro.
idade = int(input("Digite a idade da aluna: "))

# O programa então pede a altura da aluna. Como a altura pode ser um número decimal, ela é convertida para um número flutuante.
altura = float(input("Digite a altura da aluna (em metros): "))


# O programa pede ao usuário para inserir os hobbies da aluna. Os hobbies são separados por vírgulas e armazenados como uma lista.
hobbies = input("Digite os hobbies da aluna (separados por vírgula): ")
hobbies1 = hobbies.split(",")

# O programa coleta o endereço da aluna. O endereço é armazenado como uma tupla, que é uma coleção ordenada e imutável de itens.
endereco_rua = input("Digite o nome da rua: ")
endereco_numero = int(input("Digite o número do endereço: "))
endereco_cidade = input("Digite a cidade: ")
endereco = (endereco_rua, endereco_numero, endereco_cidade)

# O programa coleta o e-mail e o número de telefone da aluna. Essas informações são armazenadas em um dicionário, que é uma coleção de pares chave-valor.
email = input("Digite o e-mail da aluna: ")
telefone = input("Digite o telefone da aluna: ")
contato = {"email": email, "telefone": telefone}


# Finalmente, o programa exibe todas as informações coletadas.
print("\nInformações da aluna:")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Hobbies:", hobbies)
print("Endereço:", endereco)
print("Contato:", contato)
