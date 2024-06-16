# Tema da Aula

Na pasta `Gabrielle`, mais especificamente no arquivo `gerador_nomes.py`, foi criado um gerador de nomes divertidos baseado no horóscopo chinês.

### Instruções

Este projeto contém um gerador de nomes divertidos, utilizando três parâmetros principais:

1. **Animal do Zodíaco Chinês**: Determinado pelo ano de nascimento.
2. **Elemento do Zodíaco Chinês**: Determinado pelo ano de nascimento.
3. **Estação do Ano Chinesa**: Determinada pelo dia e mês de nascimento.

### Funcionamento do Código

O código solicita ao usuário as seguintes informações:

- Ano de nascimento
- Dia do nascimento
- Mês do nascimento

## Atividade Proposta

A atividade proposta era pegar três entradas do usuário e fazer um gerador de nomes divertido, unindo essas respostas.



##### Animal do Zodíaco

O ano de 1924 é do animal Rato, depois passa para o ano do Boi, Tigre, Coelho, Dragão, Serpente, Cavalo, Carneiro, Macaco, Galo, Cão e Porco, sucessivamente, até recomeçar o ciclo com o Rato novamente. Para determinar o animal do zodíaco baseado no ano de nascimento, pesquisei os possíveis métodos e escolhi o seguinte: subtrair 1924 do ano de nascimento e calcular o resto da divisão por 12. O resultado do resto será o índice que corresponde a um animal na lista dos animais do zodíaco chinês.

Por exemplo, se pegarmos o ano de 2009, subtrairmos 1924 e dividirmos o resultado por 12, o resto será 1, correspondendo ao segundo item da lista, ou seja, o Boi. Resto 0 retorna o Rato, resto 1 retorna o Boi, resto 2 retorna o Tigre, e assim por diante.



##### Elemento do Zodíaco

Seguindo a mesma lógica, consegui determinar o elemento do zodíaco. De acordo com o horóscopo chinês:

- Anos terminados em 0 ou 1: Metal
- Anos terminados em 2 ou 3: Água
- Anos terminados em 4 ou 5: Madeira
- Anos terminados em 6 ou 7: Fogo
- Anos terminados em 8 ou 9: Terra

Dessa forma, se eu pegar o último dígito do ano e dividi-lo por 2 utilizando a divisão inteira, terei um índice que corresponderá ao elemento, visto que cada um deles possui dois números finais correspondentes, começando no Metal e terminando em Terra. Por isso a expressão: `[(ano % 10) // 2]`.

##### Estação

Para calcular a estação do nascimento, utilizei uma estrutura de `if` e `elif`, levando em consideração os períodos de duração de cada estação. Não sei se essa é a forma mais eficiente de realizar esse cálculo, mas durante o curso espero aprender formas de otimizar meus códigos.

### O que aprendi

Com essa atividade, coloquei em prática alguns conceitos, como:

- O operador `%` que retorna o resto da divisão.
- Funções
- Índices
- Listas

Também compreendi como utilizar uma expressão que retorna um índice que corresponde a um elemento da lista.