import GraficosFunctions


def Menu():
    print(" \n \n Cinematicas Python | Proyecto de FISICA | Colegio Tabancura ")
    print("Juan Vial     |      Borja Larrain    | Profesor : Don Freddy Sanchez   |     III medio C \n ")
    sel = int(input("""Selecciona uno de los siguientes items (Numero)
    1) Calculo Bala
    2) Calcula Auto/s \n"""))
    if sel == 1:
        print("En un plano bidimensional se dispara un proyectil en tiempo 0 y posicion 0, 0. Ingrese el angulo de tiro y velocidad inicial para determinar en que punto la bala llega a su alcance maximo.")
        GraficosFunctions.FunBala(int(input("Ingrese el angulo de tiro : ")), int(input("Ingrese la velocidad >>>  ")))
    elif sel == 2:
        print('''Hay dos autos viajando en la misma direccion y sentido en un plano unidimensional. El auto 2 va x metros mas adelante que el auto 1. La idea de este programa es calcular el tiempo en que el auto A se demora en alcanzar al auto B y el punto de interseccion de los dos autos.''')
        GraficosFunctions.FunAutos(int(input("Ingrese la velocidad del auto 'A' >>>  ")), int(input("Ingrese la velocidad del auto 'B' >>>  ")), int(input("Ingrese la aceleracion del auto 'A' >>>  ")), int(input("Ingrese la aceleracion del auto 'B' >>>  ")), 0, int(input("Ingrese la distancia del auto 'B' del auto 'A' >>>  ")))
    else:
        print("Seleccion invalida")
Menu()