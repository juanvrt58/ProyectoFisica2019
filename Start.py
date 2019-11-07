import matplotlib.pyplot as pit
import numpy as np 
import GraficosFunctions


def Menu():
    print(" \n \n Cinematicas Python | Proyecto de FISICA | Colegio Tabancura ")
    print("Juan Vial     |      Borja Larrain    | Profesor : Don Freddy Sanchez   |     III medio C \n ")
    sel = int(input("""Selecciona uno de los siguientes items (Numero)
    1) Calculo Bala
    2) Calcula Auto/s
    3) Calculo Objeto que cae \n >>> """))
    if sel == 1:
        print('''Hay dos autos viajando en la misma direccion y sentido en un plano unidimensional. El auto 2 va x metros mas adelante que el auto 1. La idea de este programa es calcular el tiempo en que el auto A se demora en alcanzar al auto B y el punto de interseccion de los dos autos.''')
        GraficosFunctions.FunBala(int(input("Ingrese el angulo de tiro : ")), int(input("Ingrese la velocidad >>>  ")), int(input("Ingrese la aceleracion >>>  ")))
    elif sel == 2:
        GraficosFunctions.FunAutos(int(input("Ingrese la velocidad del auto 'A' >>>  ")), int(input("Ingrese la velocidad del auto 'B' >>>  ")), int(input("Ingrese la aceleracion del auto 'A' >>>  ")), int(input("Ingrese la aceleracion del auto 'B' >>>  ")), 0, int(input("Ingrese la distancia del auto 'B' del auto 'A' >>>  ")))
    elif sel == 3:
        GraficosFunctions.ObjetoCae("Objeto que cae", input("Ingresa el peso >>>  "), input("Ingresa la gravedad >>>  "), int(input("Ingresa la altura inicial >>>  ")))
    else:
        print("Seleccion invalida")
Menu()