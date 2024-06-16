### 1. CRIAÇÃO DO PROGRAMA
        1. Foram seguidos os passos indicados na Aula 02 do curso de análise de dados com phyton da {reprograma}
    
    2. Foi realizado um fork de um repositório indicado pela professora
    
    3. Na sequência foi criado um clone do repositório na máquina
    
    4. Foi aberta uma pasta específica com o nome da aluna, no caso JessicaBom
    
    5. Dentro dessa pasta foram criados 2 arquivos, sendo um deles:
        a. "geradorDeNomes.py"  local em que foi desenvolvido o código
        b. "README.md": refere-se ao presente local para descrever como foi implementado o programa  
    
    6. Esse programa foi criado apenas com operadores simples do Phyton, ou seja não foram usadas funções ou outros recursos mais avançados de Phyton.
    
    7. A única funcionalidade utilizada foi a formatação (f) antes do resultado para permitir mesclar os dados da string com o resultado das variáveis.

### 2. FUNCIONAMENTO DO PROGRAMA
    1. Ao ser iniciado o programa apresenta uma frase de apresentação para dar instruções ao usuário.
    
    2. O programa cria 03 variáveis distintas, sendo:
        a. superHeroi
        b. sentimentoFimDoDia
        c. lugar
    Para todas as variáveis é solicitado ao usuário que entre com palavras à sua escolha, por meio do comando input

    3. Após escolhidos o nome, o programa retorna uma frase de resultado com o nome de Super Herói Proletário. É nesse comando utilizando print que foi utilizada a função de formatação para permitir a combinação das variáveis dentro da String do resultado.

### 3. COMO EXECUTAR O CÓDIGO
Para executar esse código é necessário que você tenha instalado em seu computador o python, o git e o VSCode.
Você irá abrir um novo arquivo no VSCode,  obrigatoriamente com extensão .py e colar o código abaixo (entre os pontos:)

        ...............................................................
        print("\nDESCUBRA O SEU NOME DE SUPER HERÓI PROLETARIADO")
        print("Basta seguir os comandos")

        superHeroi = input("\nDigite o nome de um super herói (Marvel, DC, de animes) que você se identifique: ")
        sentimentoFimDoDia = input("\nEscreva o sentimento mais comum que você tem ao fim de um dia de trabalho: ")
        lugar = input("\nDigite um lugar, pode ser onde você mora, onde que morar, ou o último lugar pra onde viajou: ")

        print(f"\nSeu nome de Super Herói Proletário é: {superHeroi} {sentimentoFimDoDia} de {lugar} !")
          ...............................................................

Após isso você deverá abrir um terminal no VSCode e digitar o comando "python NOME_DO_SEU_ARQUIVO.py" e seguir as instruções
    ***OBS1: Substitua NOME_DO_SEU_ARQUIVO pelo nome que você atribuiu ao arquivo criado***
    ***OBS2: caso o comando python não funcione no terminal, substitua-o com py ou python3***