# Gerador de Nome Gamer

Minha inspiração para fazer esse programa foram aquelas imagens que dão um nome de acordo com a sua data de aniversário. Escolhi um nome gamer pois, sim, sou gamer. kkkkkk

Meu maior desafio foi pensar em nomes e adjetivos neutros e que teriam relação ao mundo dos games.

## Implementação

O programa possui três partes:

1. **Entrada de Dados:** Utilizando o input, o usuário insere a sua data de nascimento, mês de nascimento e o último digito do ano de nascimento.

2. **Lógica de Geração de Nome:** Fiz a função gerador_de_nomes() que utiliza as informações fornecidas pelo usuário para formar os três componentes do nome de gamer:

​	O primeiro componente é determinado pelo mês de nascimento. Reduzi para 4 opções de 	nomes, então utilizei o "or" para auxiliar nessa parte. (1-3 = Serpente,  4-6 = Fênix, 7-9 = 	Zumbi e 10-12 = Fantasma)

​	O segundo componente é determinado pela data de nascimento (1-5 = Mutante , 6-10 = I	nvencível, 11-15 = Invisível, 16-20 = Líder, 21-25 = Noob e 26-31 = Hacker).

​	O terceiro componente é determinado pelo último número do ano de nascimento (0-3 = 	Biruta, 4-6 = Tiltado, 7-9 = Overpower).

3. **Exibição do Resultado:** O programa imprime o nome de gamer completo, combinando os três componentes gerados. Confesso que essa parte foi a mais complicada para mim, pois no final o programa não exibia o nome. Foi quando eu pesquisei bastante e entendi que para utilizar as variáveis declaradas fora da função devo utilizar o "global nome1, nome2, nome3" para conseguir alterá-las.

   A função termina com o "return" para retornar os três nomes gerados.

   Por fim, o último desafio foi printar o nome no final, também pelejei para fazer isso. E aí entendi que deveria utilizar novas variáveis para os nomes que "saem" da função gerador_de_nomes, então criei as variáveis "nome1_gerado, nome2_gerado, nome3_gerado"


Espero que gostem!



