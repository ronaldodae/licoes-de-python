# simulador de dado
# simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layoutmontar
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]
  
    def Iniciar(self):
         # criar uma janela
        self.janela = sg.Window('Simulador de Dado',self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('agradecemos')
            else:
                print('favor clicar sim ou nao')
        except:
             print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
