class NomeDaClasse():
    pass

obj = NomeDaClasse()

class NomeDaClasse():
    """Criando um atributo de classe"""
    atributo_de_class = '123445'

obj = NomeDaClasse()

#acessando atributo de class
NomeDaClasse.atributo_de_class
#acessando o atributo a partir do objeto
obj.atributo_de_class

class NomeDaClasse():

    #construtor
    def __init__(self, x):
        self.atributo_de_instancia = x

x = 10
#criando uma instância da classe
obj = NomeDaClasse(x)


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