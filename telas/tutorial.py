from tkinter import *
import re
from os import listdir
from os import path

class Tutorial():
    def __init__(self, tela, design, idioma, interface_idioma, icon):
        self.tela = tela
        self.design = design

        LARGURA = int(tela.winfo_screenwidth() / 6)
        t_heigth = tela.winfo_screenheight()


        self.fr_texto = Frame(tela, width=LARGURA)
        self.fr_texto.grid_columnconfigure(1, weight=1)
        self.fr_texto.rowconfigure(2, weight=1)
        
        self.barra_superior = Frame(self.fr_texto, self.design.get("tutorial_barra_superior"))
        self.barra_superior.grid(row=1, column=1, sticky=NSEW)

        self.fr_principal = Frame(self.fr_texto)
        self.fr_principal.grid_columnconfigure(1, weight=1)
        self.fr_principal.rowconfigure(1, weight=1)

        self.tx_tutorial = Text(self.fr_principal, self.design.get("tutorial_tx_tutorial"), wrap=WORD)
        self.ys = Scrollbar(self.fr_principal, orient='vertical', command=self.tx_tutorial.yview)
        self.tx_tutorial.configure(yscrollcommand=self.ys.set)
        
        self.tx_tutorial.grid(row=1, column=1, sticky=NSEW)
        self.ys.grid(row=1, column=2, sticky=NS)
        self.fr_principal.grid(row=2, column=1, sticky=NSEW)

        self.dir_file = 'tutoriais/pt-br/'
        self.arquivos = listdir(self.dir_file)
        self.arquivos.sort(reverse=False)
        self.posicao = -1
        
        self.fr_botoes = Frame(tela, self.design.get("tutorial_fr_botoes"))
        self.fr_botoes.grid_columnconfigure((1,2), weight=1)

        self.botao_anterior = Button(self.fr_botoes,  self.design.get("tutorial_botao_anterior"), text="{:^22}".format(""), command=lambda: self.anterior())
        self.botao_anterior.grid(row=1, column=1, stick=NSEW)

        self.botao_proximo = Button(self.fr_botoes,  self.design.get("tutorial_botao_proximo"), text='{:^22}'.format("Proxima Aula"), command=lambda: self.proximo())
        self.botao_proximo.grid(row=1, column=2, stick=NSEW)

        self.proximo()


    def proximo(self):
        if self.posicao == len(self.arquivos)-1:
            return 0

        self.posicao += 1
        print(self.posicao,  self.arquivos[self.posicao])
        arquivo = path.join(self.dir_file, self.arquivos[self.posicao])

        self.escrever_tutorial(arquivo)

        if self.posicao == len(self.arquivos)-1:
            self.botao_proximo['text'] = '{:^22}'.format("Finalizar Tutorial")
        elif self.posicao != 0:
            self.botao_anterior['text'] = '{:^22}'.format('Voltar Aula')

    def anterior(self):
        if self.posicao < 1:
            return 0

        self.posicao -= 1
        print(self.posicao, self.arquivos[self.posicao])

        arquivo = path.join(self.dir_file, self.arquivos[self.posicao])

        self.escrever_tutorial(arquivo)

        if self.posicao > 1:
            self.botao_proximo['text'] = '{:^22}'.format("Proxima Aula")
        elif self.posicao == 0:
            self.botao_anterior['text'] = '{:^22}'.format(' ')


    def ler_tutorial(self, dir_arquivo):
        with open(dir_arquivo, 'r', encoding='utf-8') as file:
            texto_tutorial = file.read()

        linhas = texto_tutorial.split('\n')
        inicio_codigo = False
        acoes = []
        texto_codigo = ""
        for linha in linhas:



            if linha == '```' and not inicio_codigo:
                inicio_codigo = True
                continue

            if inicio_codigo and linha != '```':
                texto_codigo = texto_codigo + linha + '\n'
                continue

            if inicio_codigo and linha == '```':
                inicio_codigo = False
                acoes.append(['codigo', texto_codigo])
                texto_codigo = ""
                continue


            texto = linha.strip()

            if texto.startswith('- ['):
                linha = re.search('.*\\[(.*)\\]', texto)
                acoes.append(['lista', linha.group(1)])

            elif texto.startswith('####'):
                linha = re.search('#{1,}\\s*(.*)', texto)
                acoes.append(['subtitulo2', linha.group(1)])

            elif texto.startswith('###'):
                linha = re.search('#{1,}\\s*(.*)', texto)
                acoes.append(['subtitulo1', linha.group(1)])

            elif texto.startswith('##'):
                linha = re.search('#{1,}\\s*(.*)', texto)
                acoes.append(['subtitulo', linha.group(1)])

            elif texto.startswith('#'):
                linha = re.search('#{1,}\\s*(.*)', texto)
                acoes.append(['titulo', linha.group(1)])

            elif texto.startswith('*'):
                linha = re.search('\\*\\*(.*)\\*\\*', linha)
                acoes.append(['negrito', linha.group(1)])

            elif texto.startswith(';'):
                continue
            else:
                acoes.append(['texto', linha])

        return acoes

    def escrever_tutorial(self, dir_arquivo):

        self.tx_tutorial.configure(state=NORMAL)

        self.tx_tutorial.delete('1.0', END)

        acoes = self.ler_tutorial(dir_arquivo)

        #self.tx_tutorial.window_create(END, window = 
        #    Label(self.tx_tutorial, image = img, bg='blue')
        #)

        for acao in acoes:


            if acao[0] == 'lista':
                self.tx_tutorial.insert(END, '\n* {}'.format(acao[1]), ('texto'))

            elif acao[0] == 'titulo':
                self.tx_tutorial.insert(END, '\n{}'.format(acao[1]), ('titulo'))

            elif acao[0] == 'subtitulo':
                self.tx_tutorial.insert(END, '\n{}'.format(acao[1]), ('subtitulo'))

            elif acao[0] == 'texto':
                self.tx_tutorial.insert(END, '\n{}'.format(acao[1]), ('texto'))

            elif acao[0] == 'negrito':
                self.tx_tutorial.insert(END, '\n{}'.format(acao[1]), ('negrito'))

            elif acao[0] == 'codigo':
                self.tx_tutorial.insert(END, '\n{}'.format(""), ('texto'))
                self.tx_tutorial.insert(END, '{}'.format(acao[1]), ('codigo'))
                self.tx_tutorial.insert(END, '\n{}'.format(""), ('texto'))



        self.tx_tutorial.tag_configure('titulo', self.design.get("tutorial_tag_titulo"))
        self.tx_tutorial.tag_configure('subtitulo',  self.design.get("tutorial_tag_subtitulo"))
        self.tx_tutorial.tag_configure('subtitulo1',  self.design.get("tutorial_tag_subtitulo1"))
        self.tx_tutorial.tag_configure('subtitulo2',  self.design.get("tutorial_tag_subtitulo2"))

        self.tx_tutorial.tag_configure('texto',  self.design.get("tutorial_tag_texto"))
        self.tx_tutorial.tag_configure('negrito', self.design.get("tutorial_tag_negrito"))

        self.tx_tutorial.tag_configure('codigo', self.design.get("tutorial_tag_codigo"))



        self.tx_tutorial.insert(END, '\n')
        self.tx_tutorial.configure(state=DISABLED)
        #self.tx_tutorial.see(END)



