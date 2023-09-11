from casilla import *

import sys
import os

class listaCasillas:
    def __init__(self):
        self.primero = None
        self.columnas = 0
        self.filas = 0
        self.contadorCasillas = 0


    def insertarCasilla(self,casilla):
        if self.primero == None:
            self.primero = NodoCasilla(casilla)
            self.contadorCasillas += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoCasilla(casilla)
            self.contadorCasillas += 1 


        
    def imprimir_lista(self):
        actual = self.primero
        while actual != None:
            #print("fila: ",actual.casilla.fila, " columna: ",actual.casilla.columna," ",actual.casilla.color)
            actual = actual.siguiente



    def iniciar_tablero(self,filas, columnas,color):
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                self.insertarCasilla(Casilla(i,j,color))


    
    def actualizar(self,fila, columna, color):
        actual = self.primero
        while actual != None:
            if actual.casilla.fila == fila and actual.casilla.columna == columna:
                actual.casilla.color = color
                #print("casilla actualizada")
                return
            actual = actual.siguiente



    def devolver_color(self,fila,columna):
        actual = self.primero
        while actual != None:
            if actual.casilla.fila == fila and actual.casilla.columna == columna:
                if actual.casilla.color == "⊛":
                    actual.casilla.color = "white"
                return actual.casilla.color 
            actual = actual.siguiente



    def imprimir_tablero(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                colorn =""
                if self.devolver_color(i,j) == "white":
                    colorn = "⊛"
                if self.devolver_color(i,j) == "red":
                    colorn = "R"
                if self.devolver_color(i,j) == "blue":
                    colorn = "A"
                if self.devolver_color(i,j) == "green":
                    colorn = "V"
                if self.devolver_color(i,j) == "purple":
                    colorn = "P"
                if self.devolver_color(i,j) == "orange":
                    colorn = "N"
                print(colorn,end="\t")
            print("")
        print("")

    
    def graficar(self):
        f = open("C:/Users/81vv00k9gj/OneDrive/Escritorio/practica1/a.dot","w")
        texto="digraph G {\n node [shape=plaintext];\nlabel=\"\";\nsome_node [\nlabel=<\n<table border=\"0\" cellborder=\"0\" cellspacing=\"0\" width=\"100%\" height=\"100%\">\n"
        for i in range(1, self.filas + 1):
            texto+="<tr>\n"
            for j in range(1, self.columnas + 1): 
                texto+="<td bgcolor=\""+self.devolver_color(i,j)+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>\n];\n}"
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng C:/Users/81vv00k9gj/OneDrive/Escritorio/practica1/a.dot -o  C:/Users/81vv00k9gj/OneDrive/Escritorio/practica1/Tablero.png')
        