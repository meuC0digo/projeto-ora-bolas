
import math
import tkinter
from tkinter import CENTER, INSERT, scrolledtext
from turtle import pos

class Robo:
    def __init__(self, posx_init, posy_init):
        
        self.aceleracao = 0
        self.ax = 0
        self.ay = 0
        self.velx = 0
        self.vely = 0
        self.posy = posy_init
        self.posx = posx_init
        self.i = 0
    
    def perseguir(self):
        self.aceleracao = 2.8*tempo[1]
        self.deltax = abs(pos_x[self.i] - self.posx)**2
        print(self.deltax)

        self.deltay = abs(pos_y[self.i] - self.posy)**2
        print(self.deltay)
        somaDeltas = (self.deltax) + (self.deltay)
        print(somaDeltas)
        self.distancia = math.sqrt(somaDeltas)
        print(self.distancia)
        self.cos = (pos_x[self.i] - self.posx)/self.distancia
        self.sen = (pos_y[self.i] - self.posy)/self.distancia
        self.ax = self.cos*self.aceleracao
        self.ay = self.sen*self.aceleracao
        if (2.8 >= (self.velx + self.ax)):
            self.velx += self.ax
        else:
            self.velx = 2.8
        
        if (2.8 >= (self.vely + self.ay)):
            self.vely+=self.ay
        else:
            self.vely = 2.8
        
        self.posx += self.velx
        self.posy += self.vely


janela = tkinter.Tk()

janela.title("Robo artilheiro")

janela.geometry("800x600")

campo_pos = scrolledtext.ScrolledText(janela, width=150, height=20)
campo_pos.place(relx=0.51, rely=0.5, anchor=CENTER)

trajetoria = open("trajetoria.txt", "r")
lista_pos = []
pos_x = []
pos_y = []
tempo = []
pos_robo = []

for line in trajetoria:
    linha = line.replace("\t"," ").replace("\n"," ").replace(",", ".")
    linha2 = linha.split(" ")
    lista_pos.append(linha)
    # if linha2[1].isdigit():
    tempo.append(linha2[0])
    pos_x.append((linha2[1]))
    pos_y.append((linha2[2]))

del pos_y[0], pos_x[0], tempo[0]

for indice in range(len(pos_x)):
    pos_x[indice] = float(pos_x[indice])
    pos_y[indice] = float(pos_y[indice])
    tempo[indice] = float(tempo[indice])

trajetoria.close()
robo = Robo(9, 5)

while True:
    # print("x bola: %f - y bola: %f" % (pos_x[robo.i], pos_y[robo.i]))
    pos_robo.append("tempo: %f --- x robo: %f - y robo: %f --- x bola: %f - y bola: %f\n" % (tempo[robo.i],robo.posx, robo.posy, pos_x[robo.i], pos_y[robo.i]))
    
    robo.perseguir()
    robo.i+=1
    
    if robo.i >= len(pos_x):
        break

for line in pos_robo:
    campo_pos.insert(INSERT, line)

# print(pos_x)
# print(pos_y)
# print(tempo)





janela.mainloop()

