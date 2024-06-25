def geradorNome():
    cor = input('Digite o nome de uma cor: ')
    animal = input('Digite o nome de um animal: ')
    sobremesa = input('Digite o nome de uma sobremesa: ')
    planta = input('Digite o nome de uma planta: ')
    
    nomeEngras = print(f'Olá {cor} {animal} {sobremesa} de {planta} !')
    return(nomeEngras)

geradorNome()