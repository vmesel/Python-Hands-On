# Funções
Toda linguagem de programação tem uma forma de receber inputs e processa-los, gerando um novo output. Para este tipo de coisa, foi criado o conceito de funções na matemática que se extendeu até a computação nos dias de hoje.

A estrutura de uma função é simples:

```python
def nome_da_funcao(parametro1, parametro2 ...):
  #faz alguma ação com os parâmetros
  return valor_novo
```
Um exemplo bem simples de função é o seguinte:
```python

def soma(num1, num2):
  novo_valor = num1 + num2
  return novo_valor
```

Lembrando, os nomes de variáveis não são fixos e não precisam ser os mesmos que uma função recebe de input, mas devem ser colocados na ordem de chamada dessa função ou nomeando os como nos exemplos abaixo:

```python
print(soma(1,2))

```

```python
print(soma(num1=1, num2=2))
```
[<- Variáveis](variaveis.md) - [If e Else ->](if-else.md)
