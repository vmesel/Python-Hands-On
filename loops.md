#Loops
Os loops são uma forma de manter seu programa rodando eternamente até que uma certa condição seja realizada/completada

Existem três tipos de loop em Python:
 - While Loop: loop que, como na própria tradução do termo diz, acontece ENQUANTO algo
 - For Loop: loop que executa várias vezes e gerencia a variável de loop
 - Loops "Nesteados": Loops que se encontram dentro de um outro loop

## Loop While

O loop while é muito intuitivo, ele acontece enquanto obedecer uma certa condição!
Por exemplo, eu quero que o loop ocorra enquanto o número X for menor que 10

```python
X = 0
while X < 10:
  print(X)
  X = X + 1
```

O loop while se resume a isso

```python
while CERTA_CONDIÇÃO:
  #Faça isso
```

O loop se quebrará automaticamente até que a condição que você quer seja realizada, mas caso você queira quebrar esta condição no meio do loop, use o _break_ como no exemplo a seguir:

```
X = 0
while X < 100:
	print(X)
	X = X + 1
	if X == 10:
		break
```

## Loops for:

Loops for são tradicionalmente usados quando você precisa que uma instrução seja repetida certo número de vezes.
```
lista = ["amarelo", "vermelho", "verde"]

for x in lista:
	print(x)
``

[<- If e Else](if-else.md) - [Classes ->](classes.md)
