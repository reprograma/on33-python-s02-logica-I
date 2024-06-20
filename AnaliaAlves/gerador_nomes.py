def comeco(mensagem):
    return input(mensagem)

def final(nome, objeto, cor, sentimento):
    return f"Seu nome divertido é: {nome} {objeto} {cor} {sentimento}"

def gerar_nome_divertido():
    print("Bem-vindo ao gerador de nomes divertidos!")
    
    nome = comeco("Insira Seu Primeiro Nome: ")
    objeto = comeco("Insira Um Objeto: ")
    cor = comeco("Insira Uma Cor: ")
    sentimento = comeco("Insira Um Sentimento: ")
    
    nome_divertido = final(nome, objeto, cor, sentimento)
    print(nome_divertido)

gerar_nome_divertido()

