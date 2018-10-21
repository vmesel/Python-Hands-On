# Pacotes PIP

PIP é um sistema gerenciador de pacotes da linguagem de programação Python. Ele é usado para gerenciar e instalar
pacotes caso sua aplicação necessite. Nos pacotes você obtêm módulos, e módulos são bibliotecas de arquivos escritos em Python
que você pode incluir no seu projeto.

# Instalação

Se possuir Python 2.7.9+/3.4+ em sua máquina o pip já vem como default(padrão). 
Para verificar se possui pip e qual a versão digite o seguinte comando no seu terminal:
```
$ pip --version
pip 18.0 from /local/to/python/site-packages/pip (python 2.7)
```
No caso acima a versão do pip é 18.0.

# Utilização

Para você poder usufruir dos pacotes que estão indexados no PyPI(Python Package Index - https://pypi.org/), basta utilizar os
seguintes comandos:

Para instalar um pacote:
```
$ pip install nome-do-pacote
```
Para desinstalar um pacote:
```
$ pip uninstall nome-do-pacote
```

Após várias instalações de pacotes, precisamos manter controle sobre eles e as versões em que os pacotes se encontram, para que futuramente não ocorra algum tipo de conflito e você possa gerenciar melhor seu software.

O comando utilizado para visualizar os pacotes e suas versões é:
```
$ pip freeze

Django==1.11.13
django-allauth==0.36.0
oauthlib==2.1.0
Pillow==3.3.1
psycopg2==2.7.4
```
Porém para mantermos melhor o controle dos pacotes, precisamos guardar essas informações em um lugar onde você possa utilizar 
caso queira instalar seu software em outra máquina ou servidor.
Sendo assim utilizaremos o seguinte comando:
```
$ pip freeze > requirements.txt 
```
Finalizado, poderá ver que foi criado um arquivo .txt com o nome de requirements(requerimentos), que como o próprio nome já diz, são os pacotes requeridos/utilizados no seu programa.
Caso queira instalar o requirements.txt de algum programa ou testar o seu próprio basta utilizar o comando:
```
$ pip install -r requirements.txt 
```

# Atualização

Sempre é indicado manter programas e pacotes atualizados, é normal aparecer uma mensagem dessa no terminal
```
You are using pip version 10.0.1, however version 18.0 is available.
```
Para atualizar basta utilizar o comando:
```
pip install --upgrade pip
```

Esses são os passos básicos para começar com o pip. Agora é explorar os 146,971 projetos que ele possui.
