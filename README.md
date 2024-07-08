<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Introdução ao Python e Conceitos Básicos

Turma Online 33 | Semana 2 | 2024 | Professora [Jenifer Plácido](https://www.linkedin.com/in/jenifer-pl%C3%A1cido-00b5611ab/)

# 🌟 Introdução ao Python e Conceitos Básicos 🌟

## 📚 Tópicos Abordados

1. **Introdução **
2. **Tipos de Valores e Variáveis**
3. **Inputs**
4. **Operadores**
5. **Formatação**
6. **Funções**
7. **Links Úteis**

---

## 1. Introdução 🧭

Python é uma linguagem de programação versátil e fácil de aprender, amplamente utilizada em diversas áreas como desenvolvimento web, ciência de dados, automação e inteligência artificial. Mesmo se você nunca programou antes, não se preocupe! Este guia vai te ajudar a dar os primeiros passos.

### Por que aprender Python?

- **Fácil de aprender**: Sintaxe simples e clara.
- **Versátil**: Usada em muitas áreas diferentes.
- **Comunidade acolhedora**: Suporte e recursos disponíveis.

---

## 2. Tipos de Valores e Variáveis 📊

### Tipos de Valores

- **Inteiros (`int`)**: Números inteiros como `1`, `42`, `-3`.
- **Ponto Flutuante (`float`)**: Números decimais como `3.14`, `-0.001`.
- **Strings (`str`)**: Sequências de caracteres como `"Olá, mundo!"`.
- **Booleanos (`bool`)**: Verdadeiro (`True`) ou Falso (`False`).

### Variáveis

Variáveis são como "caixas" onde você pode guardar valores para usar depois.

#### Exemplo:

```python
nome = "Jenifer"  # Variável do tipo string
idade = 34  # Variável do tipo inteiro
altura = 1.67  # Variável do tipo float
```

#### Dicas

- Escolha nomes de variáveis que façam sentido.
- Evite usar palavras reservadas do Python como nomes de variáveis.

---

## 3. Inputs 🎤

Para interagir com o usuário e obter informações, usamos a função `input()`.

### Exemplo:

```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Convertendo idade para inteiro
idade = int(idade)

print(f"Olá, {nome}! Você tem {idade} anos.")
```

#### Nota

- `input()` sempre retorna uma string. Converta para outros tipos conforme necessário.

---

## 4. Operadores ➕

### Operadores Aritméticos

- **Adição (`+`)**, **Subtração (`-`)**, **Multiplicação (`*`)**, **Divisão (`/`)**, **Exponenciação (`**`)**.
- **Módulo (`%`)**: Resto da divisão.
- **Divisão Inteira (`//`)**: Quociente da divisão inteira.

#### Exemplo:

```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a % b)  # 1
print(a ** b)  # 1000
print(a // b)  # 3
```

### Operadores de Comparação e Lógicos

- **Igual (`==`)**, **Diferente (`!=`)**, **Maior (`>`)**, **Menor (`<`)**.
- **Maior ou Igual (`>=`)**, **Menor ou Igual (`<=`)**.
- **E (`and`)**, **Ou (`or`)**, **Não (`not`)**.

#### Exemplo:

```python
a = 10
b = 3

print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False
print(a and b)  # True
print(a or b)  # 10
print(not a)  # False
```

---

## 5. Formatação ✨

Formate strings para exibir informações de maneira clara e organizada usando `f-strings` e métodos de strings.

### `f-strings`

Use `f-strings` para inserir variáveis dentro de strings.

#### Exemplo:

```python
nome = "Jenifer"
idade = 34
altura = 1.67

print(f"Meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura} metros.")
```

### Métodos de Strings

- **`.upper()`**, **`.lower()`**, **`.title()`**.
- **`.strip()`**, **`.replace(old, new)`**, **`.find(sub)`**.

#### Exemplo:

```python
texto = " Olá, mundo! "

print(texto.upper())  # " OLÁ, MUNDO! "
print(texto.lower())  # " olá, mundo! "
print(texto.title())  # " Olá, Mundo! "
print(texto.strip())  # "Olá, mundo!"
print(texto.replace("mundo", "Python"))  # " Olá, Python! "
print(texto.find("mundo"))  # 6
```

---

## 6. Funções 📋

### Funções em Python

Funções são blocos de código reutilizáveis que executam uma tarefa específica.

#### Funções com Retorno

Funções que retornam um valor após a execução.

##### Exemplo:

```python
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # 8
```

#### Funções sem Retorno

Funções que executam uma ação sem retornar um valor.

##### Exemplo:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Jenifer")  # Saída: "Olá, Jenifer!"
```

### Funções Internas de Python

Python possui várias funções internas que facilitam o desenvolvimento de software.

#### Exemplos:

- **`len()`**: Retorna o número de itens de um objeto (tamanho).

```python
texto = "Olá, mundo!"
quantidade_caracteres = len(texto)
print(f"O texto possui {quantidade_caracteres} caracteres.")
```

- **`print()`**: Exibe uma mensagem na tela ou outro dispositivo de saída.

```python
print("Olá, mundo!")
```

- **`input()`**: Obtém entrada do usuário através do teclado.

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

---

## 7. Links Úteis 🔗

- [Documentação Oficial do Python](https://docs.python.org/3/)
- [Python para Iniciantes](https://www.python.org/about/gettingstarted/)
- [Exercícios de Python](https://www.w3schools.com/python/python_exercises.asp)
- [Comunidade Python Brasil](https://python.org.br/)
- [Guia Completo de Markdown](https://www.markdownguide.org/)

---

✨ **"Vocês são incríveis! Cada linha de código escrita é um passo a mais na construção de um futuro brilhante. Continuem explorando, aprendendo e crescendo. A tecnologia precisa do talento e da paixão de cada uma de vocês. Juntas, podemos transformar o mundo!"** ✨

---

![Python Logo](https://www.vectorlogo.zone/logos/python/python-ar21.svg)

---

💡 **Dica**: Nunca parem de aprender e colaborar. A comunidade de desenvolvedoras é grande e acolhedora. Aproveitem! 🌐💻


<p align="center">
Desenvolvido com :purple_heart: por Jenifer Plácido
</p>

