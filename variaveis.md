# Variáveis

Assim como em toda linguagem de programação, o Python também trata os diferentes tipos de dados com variáveis, e existem diversos tipos de variáveis. Estes tipos são os seguintes:

 - int (Classe de Inteiros do Python);
 - float (Classe de Números decimais do Python);
 - list (Classe de arrays em Python);
 - tuple (Classe de tuplas em Python);
 - dict (Classe de dicionários em Python);
 - str (Classe de strings em Python)
 
 Como Python possui apenas a sua tipagem dinâmica, ou seja, você não precisa definir os tipos de valores de uma variável e eles podem ser mutáveis, você declara um valor de qualquer tipo da seguinte maneira
 
```
inteiro = 2
texto = "Ola Mundo"
decimal = 0.00
tupla = ("Ola", "Mundo")
dicionario = {"Ola": "Mundo"}
lista = ["primeiro item", "segundo item"]
```

Como você pode perceber, para declarar números, sejam eles ints ou floats, não é necessária a adição de aspas ao redor deles, já os demais tipos que recebem textos dentro deles é necessário que seja adicionado aspas em volta de seus textos.
Depois de montarmos estas variáveis, por que não fazemos um print de seus tipos e de seus valores 

```
print("Inteiro - Conteudo da Variavel: {} e tipo da variavel {}".format(inteiro,type(inteiro)))
print("Texto - Conteudo da Variavel: {} e tipo da variavel {}".format(texto,type(texto)))
print("Decimal - Conteudo da Variavel: {} e tipo da variavel {}".format(decimal,type(decimal)))
print("Tupla - Conteudo da Variavel: {} e tipo da variavel {}".format(tupla,type(tupla)))
print("Dicionario - Conteudo da Variavel: {} e tipo da variavel {}".format(dicionario,type(dicionario)))
print("Lista - Conteudo da Variavel: {} e tipo da variavel {}".format(lista,type(lista)))
```

PS: O comando .format() pega os valores "{}" inseridos em um texto e substitui por algum valor que você tenha interesse em colocar em conjunto com esta string, assim você não terá de ficar alterando ela a cada vez que você criar uma nova modificação.

O retorno deste código deve ser o seguinte

```
Inteiro - Conteudo da Variavel: 2 e tipo da variavel <class 'int'>
Texto - Conteudo da Variavel: Ola Mundo e tipo da variavel <class 'str'>
Decimal - Conteudo da Variavel: 0.0 e tipo da variavel <class 'float'>
Tupla - Conteudo da Variavel: ('Ola', 'Mundo') e tipo da variavel <class 'tuple'>
Dicionario - Conteudo da Variavel: {'Ola': 'Mundo'} e tipo da variavel <class 'dict'>
Lista - Conteudo da Variavel: ['primeiro item', 'segundo item'] e tipo da variavel <class 'list'>
```

E para mostrar que Python tem uma tipagem dinâmica, você pode fazer o seguinte:

```
a = "String aqui"
b = ["Lista aqui"]

print(a, b)

a, b = b, a

print(a, b)
```

Neste código nós definimos dois tipos de variáveis diferenciadas e logo em seguida, nós as colocamos na tela, após isto, nós as invertemos e colocamos na tela novamente para podermos verificar que uma variável não fica presa a um valor.

[<- Olá Mundo](ola-mundo.md) - [Funções ->](funcoes.md)
