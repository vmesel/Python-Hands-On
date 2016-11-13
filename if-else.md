#If e Else Statements
Estes são argumentos/statements para tratativa de dados, estes argumentos servem para dizer: "se algo acontecer: faça isso, se não: faça aquilo".

Existem diversas tratativas que podem ser usadas dentro de um if:
 - == : que checa se um valor é igual ao comparado
 - is : o mesmo que o anterior
 - is not: checa se o valor é diferente ao comparado
 - is None: checa se o valor é vazio
 - is not None: checa se o valor não é vazio

A estrutura simples de um IF/Else é caracterizada a seguir:
```python
if valor_a_ser_comparado atuador_de_condicao valor_comparador:
  # Faz alguma coisa aqui
```

No caso acima: o valor a ser comparado é um valor que você tem o valor; o atuador_de_condição é um daqueles comparadores mostrados na lista; o valor comparador é um valor que você sabe que é o correto e quer averiguar com ele.

Alguns exemplos de uso destes casos são:

```python
#Vamos checar se um número é igual ao outro:
x = 0
if x == 1:
  print("É igual")
else:
  print("É diferente")
  
if x is not None:
  print(x)
else:
  print("X está vazio")
```

Se os valores a serem comparados forem booleanos você pode fazer o seguinte:
```python
x = True
if x:
  print("É verdade")
else:
  print("Não é verdade")
```

[<- Funções](funcoes.md) - [Loops ->](loops.md)
