Esse material foi criado inicialmente para um workshop de duas horas e com o passar do tempo foi usado em outras demonstrações de Python. Este material rapidamente começou a receber solicitações de itens que haviam sido deixados de fora porque não cabiam no formato de duas horas e também contribuições de outros programadores que acharam o material útil.

Como crescer é inevitável, parece ser uma boa ideia abraçar essa oportunidade, e assim estender o material, tornando-o assim um repositório de códigos e exemplos que possam ser usados por todos para estudo e referência.

## Primeiros passos

Olhe as issues e veja se o que você quer fazer já não esta sendo discutido, se estiver ótimo, participe da discussão e de suas ideias, caso não esteja você pode criar uma nova issue para discutirmos ou se preferir pode também mandar diretamente um _pull request_, só não esqueça de descrever muito bem o que você quer mudar/adicionar.

## Formato

Material novo idealmente deve ser organizado em diretórios e ter três arquivos, um README.md descrevendo o exemplo, um exemplo.py contendo o exemplo propriamente dito e um exemplo_test.py.

```
exemplo/README.md
exemplo/exemplo.py
exemplo/exemplo_test.py
```

O material antigo esta aos poucos sendo reformatado para esse novo padrão.

## Cuidado com o código

Antes de mandar um _pull request_ formate seu código com _pep 8_. Também é uma boa ideia passar uma ferramenta de análise estática como _pylint_ por exemplo.

## Variáveis 

Inicialmente todas as variáveis eram escritas em inglês porque fica um código mais idiomaticamente homogêneo, mas para quem esta iniciando na linguagem é fácil confundir variáveis com palavras reservadas, então para resolver esse problema adotamos o português para nomes de variáveis. Fora do âmbito desse material é uma boa prática nomear as variáveis em inglês.


## Não se prolongue demais

Uma das características que é importante manter são exemplos curtos e de fácil entendimento, tente fazer com que os exemplos caibam em uma tela, tudo bem se não for possível, apenas mantenha isso em mente.

Exemplos rápidos, curtos, diretos e de fácil entendimento são nossa meta.

## Enviando uma contribuição

- Faça um _fork_ do projeto.
- Crie uma _branch_ com as suas modificações `git checkout -b exemplo-fantastico`.
- Faça _commit_ das suas alterações `git commit -m 'Implementação do novo exemplo fantástico'`.
- Faça um _push_ na sua _branch_ `git push origin exemplo-fantastico`.
- Faça um _pull request_ com suas alterações.
