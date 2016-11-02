# Configurando

A configuração do seu ambiente Python é a coisa mais importante para você iniciar no mundo do Python. Ela serve para seu sistema reconhecer o interpretador do Python como um programa nativo que você possa chamar através do comando:

```
$- python3
```

Para isso, nós temos de configurar o ambiente em todos os sistemas operacionais, o permitindo ser executável em todas as partes dele e nos deixando livres para trabalhar em qualquer pasta que quisermos.

---

## Windows

Para realizar esta configuração você terá que ir em: Menu Iniciar > Pesquisar > Editar as Variáveis de Ambiente do Sistema > Variáveis de Ambiente. Nesta localidade você encontrará todas as variáveis que são necessárias para que seu sistema operacional funcione corretamente, por favor, não retire nenhuma delas apenas edite a variável PATH, adicionando o seu caminho para a pasta Python e para o mesmo caminho com o fim \Scripts\

## MacOS e Linux

Se você instalou utilizando as ferramentas de gerenciamento de pacotes que são disponibilizadas nestes sistemas, estas variáveis já foram configuradas automaticamente, portanto você não precisa se preocupar, mas caso você tenha baixado o executável e instalado na mão, você precisará rodar os seguintes comandos no seu Terminal.

```
export PATH="$PATH:/caminho/para/o/python"
```
Você deve substituir este /caminho/para/o/python com todo o caminho para o executável do Python 3. Este trecho de código deve ser adicionado ao seu .bash-rc para que ele possa ser executado toda vez que seu sistema for iniciado, assim ele não perderá nunca onde o Python está

---

## Testando a instalação 

Para testar a sua instalação, bastará você rodar o comando "python" em seu terminal, caso ele retorne algo semelhante ao exemplo abaixo, seu Python está configurado plenamente! :smiley:

```
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

[<- Instalando](instalando.md) - [Olá Mundo ->](ola-mundo.md)
