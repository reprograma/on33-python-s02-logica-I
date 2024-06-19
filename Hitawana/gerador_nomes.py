def gerar_nome_divertido():
    cor = input("Olá, digite uma cor: ")
    animal = input("animal : ")
    sobremesa = input("e por ultimo, digite uma sobremesa: ")

    quant_cor = len(cor)
    quant_animal= len(animal)
    quant_sobremesa= len(sobremesa)
    corte_cor =  quant_cor // 2
    corte_animal =  quant_animal // 2
    corte_sobremesa =  quant_sobremesa // 2

    parte_cor = cor[0:corte_cor]
    parte_animal = animal[0:corte_animal]
    parte_sobremesa = sobremesa[0:corte_sobremesa]

    nov_nome1 = parte_cor + parte_sobremesa
    nov_nome2 = parte_sobremesa + parte_animal
    nov_nome3 = parte_animal + cor + parte_sobremesa
    nome_divertido = f"Seu nome divertido é:  {nov_nome1},  {nov_nome2} ,  {nov_nome3}."

    print(nome_divertido)

gerar_nome_divertido()
