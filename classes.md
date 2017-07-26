# Classes

Python é uma linguagem de múltiplos paradigmas de programação, entre eles a orientação a objetos é um dos mais conhecidos e mais usado nos últimos anos. A orientação a objeto pythônica é orientada a classe, e neste artigo nós pretendemos introduzir-lhe um pouco mais sobre as classes.

Segundo a documentação do Python, uma classe associa dados (atributos) e operações (métodos) em uma estrutura única. Um objeto é uma variável cujo tipo é uma classe, ou seja, um objeto é uma instância de uma classe.

A sintaxe para declararmos uma classe é a seguinte:

```python
class NomeDaClasse():
    pass # aqui podem vir os diversos metodos e atributos da sua classe

objeto_de_classe = NomeDaClasse()
```

A variável objeto_de_classe é um objeto da classe NomedaClasse, ou seja, uma instância dessa classe e dentro dela, podemos ter diversos atributos e métodos. Um atributo de classe, também conhecido como atributo estático, pois, seu valor é compartilhado com todas as instância (objetos).

## Atributos de classe

Para declarar um atributo de classe é igual a quando criamos uma variável, a diferença é que criamos essa variável dentro da classe, desse modo:

```py
class NomeDaClasse():
    """Criando um atributo de classe"""
    atributo_de_class = '123445'

obj = NomeDaClasse()

#acessando atributo de class
NomeDaClasse.atributo_de_class
#acessando o atributo a partir do objeto
obj.atributo_de_class
```

O acesso ao atributo da classe pode ser feito de dois modos, utilizando a própria classe ```NomeDaClasse.atributo_de_class```, ou utilizando o próprio objeto ```obj.atributo_de_class```.

## Atributos de instância

O atributo de instância é um atributo para se guardar um valor que pode ser diferente para cada objeto, não sendo compartilhado entre os objetos, como acontece com o atributo de classe.

```py
class NomeDaClasse():

    #construtor
    def __init__(self, x):
        self.atributo_de_instancia = x

x = 10
#criando uma instância da classe
obj = NomeDaClasse(x)

```

Agora nosso exemplo ficou um pouco mais complexo, e além do atributo de instância, introduzimos também um método, e para piorar tem uma palavra self como primeiro argumento.

Bom, vamos lá, detalhar passo a passo.

Primeiro, antes de mais nada, vamos entender o que significa o self.

## O parâmetro self

Este é passado explicitamente para todos os métodos, diferente de outras linguagens em que se passado implicitamente. Não se faz obrigatório usar o nome self, mas é uma convenção que se chame esse primeiro argumento de __self__.

```py
class NomeDaClasse():

    #construtor
    def metodo_qualquer(self, x):
        self.atributo_de_instancia = x

x = 10
obj = NomeDaClasse()

#chamada do método
obj.metodo_qualquer(x)
#chamada do mesmo método de modo diferente (não usual)
NomeDaClasse.metodo_qualquer(obj, x)
```

Observe-se o código acima, criamos um método qualquer e depois utilizamos duas forma diferentes de chamar o método. A primeira forma é a que devemos utilizar e a segunda forma é para exemplificar o significado do self. O self representa a instância do objeto, só que quando fazemos desta forma ```obj.metodo_qualquer()``` o python se encarrega de passar automaticamente a instância do objeto para o argumento self, já na segunda maneira estamos passando explicitamente o objeto para o argumento self.

## O construtor

Agora vamos entender o construtor ```def __init__()```. Como o próprio nome sugere o construtor constrói a classe, é executado automaticamente assim que instanciamos um objeto. Ele é usado para iniciar valores de atributos que serão utilizado na classe (quando necessário) e também para chamar métodos que necessitem ser executados apenas quando se inicia à classe.

## Conclusão e retomada ao atributo de instância

Agora finalmente podemos entender o atributo de instância, que acredito que nesse momento você já deve estar achando simples. Como sabemos o self é a instância do objeto, e o atributo de instância é quando usamos o ```self.atributo```, os valores contidos neste atributo são os valores do objeto, logo cada objeto pode ter valores diferentes para o mesmo atributo.

[<- Loops](loops.md) - [Pacotes PIP ->](pacotes_pip.md)
