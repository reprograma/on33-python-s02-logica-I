def geradorNomes():
        print('Bem-vindo ao gerador de nomes divertidos!')
        cor = input('Digite uma cor: ').capitalize()
        animal = input('Digite um animal: ').capitalize()
        danca = input('Digite uma dança: ').capitalize()
        sobremesa = input('Digite uma sobremesa: ').capitalize()
        
        nomeEngracado = print('Prazer em te conhecer', animal, sobremesa,'de', danca, cor,'!')
        return(nomeEngracado)

geradorNomes()