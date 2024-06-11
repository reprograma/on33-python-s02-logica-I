# Gerador de Nomes Divertidos com Python:

### Método 1:

* **Realizado 3 linhas de código (linhas 3, 4 e 5) para solicitar ao usuário uma entrada e armazená-la em uma variável.**
    * Exemplo:
        ```python
        cor = str(input('Informe uma cor: '))
        ```
    * Detalhes:
        * `cor`: variável para armazenar a cor digitada pelo usuário.
        * `=`: operador de atribuição (atribui o valor digitado à variável).
        * `str()`: função que converte o valor digitado para string.
        * `input('Informe uma cor: ')`: exibe a mensagem na tela e captura a entrada do usuário.

* **Declarada a variável 'nome_divertido' (linha 7) para armazenar as variáveis 'cor', 'animal' e 'sobremesa'.**
    * Objetivo: armazenar os valores em conjunto.
    * Exemplo:
        ```python
        nome_divertido = cor, animal, sobremesa
        ```

* **Gerado código na linha 9 para exibir a frase final.**
    * Combina as variáveis `cor`, `animal` e `sobremesa` em uma frase.
    * Exemplo:
        ```python
        print('Seu nome divertido é ', cor, animal, sobremesa)
        ```

* **Adicionada uma linha para melhor formatação da apresentação das 3 atividades no terminal.**
    ```python
    print('======================================================')
    ```

### Método 2:

* **Criada a função `gerar_nome_divertido()` para solicitar os dados do usuário e retornar a frase completa.**

* **Detalhes da função:**
    * Solicita a entrada do usuário e armazena em variáveis:
        ```python
        cor = str(input('Informe uma cor: '))
        ```
    * Combina as variáveis em uma string formatada:
        ```python
        nome_divertido = f"{cor} {animal} {sobremesa}"
        ```
    * Exibe a frase completa:
        ```python
        print('Seu nome divertido é ', nome_divertido)
        ```

* **Chamada da função:**
    * Executa o código dentro da função:
        ```python
        gerar_nome_divertido()
        ```

* **Adicionada uma linha para melhor formatação da apresentação das 3 atividades no terminal.**
    ```python
    print('======================================================')
    ```

### Método 3 - Utilizando random

* **Importada a biblioteca `random` para gerar dados aleatórios.**
    * Exemplo:
        ```python
        import random
        ```

* **Criadas as listas de dados para armazenar cores, animais e sobremesas para escolha aleatória.**
    * Exemplos:
        ```python
        cores = []
        animais = []
        sobremesa = []
        ```

* **Atribuição aleatória de valores às variáveis 'cor', 'animal' e 'sobremesa' usando a função `random.choice()`.**
    * Exemplos:
        ```python
        cor = random.choice(cores)
        animal = random.choice(animais)
        mesa = random.choice(sobremesa)
        ```

* **Armazenamento do nome divertido na variável `nome_divertido` usando formatação de string.**
    * Exemplo:
        ```python
        nome_divertido = f"{cor} {animal} {sobremesa}"
        ```

* **Exibição da frase final com o nome divertido gerado aleatoriamente.**
    * Exemplo:
        ```python
        print('Seu nome divertido é', nome_divertido)
        ```

* **Adicionada uma linha para melhor formatação da apresentação das 3 atividades no terminal.**
    ```python
    print('======================================================')
    ```

# COMO UTILIZAR:

* **Gerando um Nome Divertido Manualmente:**
    * Opção para quem deseja personalizar cada entrada;
    * Abra o terminal na pasta que contenha o arquivo gerador_nomes.py;
    * Digite o comando:
        ```python
        py gerador_nomes.py
        ```
    * E realize o input dos três dados solicitados;
    * Ao final será apresentado a frase 'Seu nome divertido é' + a junção das entradas aplicadas;

* **Gerando um Nome Divertido com Função:**
    * Alternativa mais organizada e reutilizável;
    * Abra o terminal na pasta que contenha o arquivo gerador_nomes.py;
    * Digite o comando:
        ```python
        py gerador_nomes.py
        ```
    * Realize o input dos três dados solicitados;
    * Ao final será apresentado a frase 'Seu nome divertido é' + a junção das entradas aplicadas;

* **Gerando um Nome Divertido Aleatoriamente:**
    * Opção para nomes divertidos surpresa;
    * Abra o terminal na pasta que contenha o arquivo gerador_nomes.py;
    * Digite o comando:
        ```python
        py gerador_nomes.py
        ```
    * Ao rodar o programa apenas irá exibir a frase 'Seu nome divertido é' + nome_divertido que conterá os valores gerados aleatóriamente com random.