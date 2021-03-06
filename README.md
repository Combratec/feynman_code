![Imagem](imagens/projeto.gif)

-------


<p align="center">
  Desenvolvimento da linguagem de programação Safira
  <br>
  <a href="https://safiralang.blogspot.com/"><strong>Faça do Download das versões estáveis >> </strong></a>
  <br>
  <br>

</p>

![GitHub estrelas](https://img.shields.io/github/stars/safira-lang/safira-ide)
![GitHub last commit](https://img.shields.io/github/last-commit/safira-lang/safira-ide?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/safira-lang/safira-ide)
![GitHub language count](https://img.shields.io/github/languages/count/safira-lang/safira-ide)
![GitHub repo size](https://img.shields.io/github/repo-size/safira-lang/safira-ide)

# Introdução

A Safira é uma linguagem de programação focada na lógica com o objetivo de amortecer o impacto do primeiro contato com o mundo da programação, oferecendo uma interface simples, intuitiva e uma codificação natural.

A Safira é focada apenas na estrutura básica e em pequenos scripts, sendo que o principal diferencial dela é aceitar comandos em níveis naturais, como se fosse uma pessoa conversando com outra e comandos em linguagem similar as principais linguagens do mercado.

Nos primeiros contatos com a Safira, é recomendado o uso de comandos no idioma nativo, como o português, exemplo:

Se o foco for ensinar linguagem Python para um grupo de pessoas com dificuldade, é recomendado começar com comandos bem simples, como:

    nome vale o que o usuario digitar

    se nome for igual a "Gabriel" entao {
        mostre "Olá Gabriel"
    } 

Posteriormente, é recomendado a variação, mesmo que seja comando por comando, no ritmo do aluno para a seguinte codificação:

    nome = input

    if nome == "Gabriel" {
        print "Olá Gabriel"
    }

Perceba que a Safira está muito mais próximo do Python agora.

Desta forma, a complexidade das linguagens de programação, é reduzida e o conceito é levado mais em conta. 

A safira entende comando em inglês, português, espanhol e de forma similar a outras linguagens do mercado.
 
É assim que fica a codificação de um programa maior na Safira.  

![Imagem](imagens/safira.png)

--------------------------------

# Para usuários

Se você só quer experimentar a Safira, está é a guia para você!

Atualmente, você precisará de um computador para usar a Safira, ainda não temos uma versão para smartphones. Baixe a última versão estável, no final da página em **Download** ou clicando [aqui]( https://safiralang.blogspot.com/p/downloads.html).

1. Baixe o arquivo .zip do Google Drive.
2. Extraia-o em alguma pasta, você precisará do [Winrar](https://www.win-rar.com/start.html?&L=0) para extrai-lo.
3. Execute a Safira!

**Para distribuições Linux, certifique de fornecer as permissões para executar. **

### Como programar em Safira?

Faça testes na interface e consulte a guia exemplos da própria IDE para ver os comandos que a Safira possui. (Atualmente não temos um tutorial passo a passo)


-------------------------------------


# Para desenvolvedores

Se você quer ajudar no desenvolvimento da Safira, este é o local para você!

### Sobre a Safira

Hoje a safira é feita no Python3.8, tenha ele instalado na máquina e com um ambiente virtual preparado. As principais plataformas de desenvolvimento e suporte da Safira é Ubuntu 20, Linux Mint e Windows 10 por enquanto. A IDE final deve ser ter menos que 30 mb, ser um executável e devendo funcionar no Windows 10 prioritariamente.

### Quem pode ajudar no desenvolvimento?

Atualmente precisamos de pessoas que possam dar feedback sobre o projeto, usá-lo para encontrar bugs, de desenvolvedores que possam melhorar o código, tornando o mais escalável, de designs para ajudar no desenvolvimento de interfaces mais bonitas e que sejam úteis para os usuários e de pessoas para colocar a mão na massa e ajudar a criar o sistema.

> Existe a pretensão da Safira mudar de linguagem?
> Sim, é uma possibilidade, mas vamos com calma.

### Interface gráfica

* A biblioteca multiplataforma Tkinter é o único recurso usado atualmente para a criação das interfaces na Safira.

### Para iniciar o desenvolvimento:

Está é uma versão de desenvolvimento, com bugs e implementações em andamento.

1. clone este repositório  
2. Baixe e instale o Python3.8 (3.7 e 3.6 são aceitos)  
3. Crie e ative um ambiente virtual   
```shell
python3.8 -m venv .
source ./activate
```
4. Instale as dependências
```shell
python -m pip install requeriments.txt
```
5. Instale novas bibliotecas
Instale as bibliotecas, dentro do ambiente virtual. Por favor, evite ao máximo bibliotecas não nativas do Python, elas podem causar problemas ao serem migradas para diferentes sistemas operacionais.
```shell
python -m pip install requests
```

6. Desenvolva!
Programe, sempre tentando separar todas as etapas, a fim de que seja possível executar as novas partes de forma independênte da IDE.

7. Salve os requisitos
```shell
python -m pip freeze > requeriments.txt
```

8. Suba no git
Suba suas alterações no GITHUB. De preferência, entre em no nosso Discord para conversarmos antes de você subir alterações.
https://discord.gg/AvSSZsVA

-----------------

# Atualmente tento seguir estes padrões

## Nomes de Widgets Tkinter

| Widgets tkinter    | Nomes de variáveis |
|--------------------|--------------------|
| Button             | bt_                |
| Label              | lb_                |
| Frame              | fr_                |
| Entry              | et_                |
| Text               | tx_                |

-------------------------

## Classes

Classes devem começar com letra maiúscula, e terem type anotations e docstring para documentá-las

```python
class Atualizar:
    """ Essa classe fornece recursos de atualizações """
    def __init__(self, versao:str) -> None:
        pass
```

------------------------

## Funções

todas as letras em **minúscula** e separado por _, usando type anotations e docstrings

```python
def analisar_comando(self, texto: str, pontos: dict={}) -> dict:
    return {'pontos': pontos}

```

-------------

### Outras boas prátcas

```python
    # Recomendado
    if (valor):

    # Nao recomendado
    if (valor == True)



    ### Recomendado
    if (valor is None):

    ### Não recomendado
    if (valor == None)



    ### Recomendado
    from requests import post

    ### Recomendado
    from requests import requests_post

    ### Não recomendado pois carrega toda a biblioteca
    import requests


    
    ### Recomendado
    try:
        ...
    except Exception as erro:
        print('Erro ao realizar coloração: ', e)

    ### Não recomendado
    try:
        ...
    except:
        pass

```

-------------------------

# Download

* [Windows 10](https://safiralang.blogspot.com/p/downloads.html)
* [Linux Mint](https://safiralang.blogspot.com/p/downloads.html)
* [Ubuntu](https://safiralang.blogspot.com/p/downloads.html)

# Outros Links

* [Blog](https://safiralang.blogspot.com/)
* [Facebook](https://www.facebook.com/safiralang/)
