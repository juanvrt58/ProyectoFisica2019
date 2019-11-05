
from  pylab import *
import numpy as np 
from math import sqrt
#from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

def ecuacioncine(v,x, t, a):
    f = x + v * t + 0.5 * a * t**2
    return f
def FunBala(Title, velocidad, aceleracion, tiempo, peso):
    Time = []
    Hight = []
    for i in range(tiempo):
        Time.append(i)
        Hight.append(i) #Llamar a formula con "i"
    pit.plot(Hight, Time)
    pit.show()  

def FunAutos(velocidad_A, velocidad_B, aceleracion_A, aceleracion_B, distancia_A, distancia_B,):
    tiempo_1, tiempo_2, tiempo_3, tiempo_4 = 0, 0, 0 ,0
    punto_interseccion_1, punto_interseccion_2 = 0, 0

    if aceleracion_B >= aceleracion_A:
        print("El auto A no alcanza al auto B")

    elif aceleracion_B < aceleracion_A:
        tiempo_1 = (-(velocidad_A - velocidad_B) + sqrt((velocidad_A - velocidad_B)**2 +(- 4) *0.5*(aceleracion_A - aceleracion_B)*(distancia_A - distancia_B))) / (aceleracion_A - aceleracion_B)

        tiempo_2 = (-(velocidad_A - velocidad_B) - sqrt((velocidad_A - velocidad_B)**2 + (-4) *0.5*(aceleracion_A - aceleracion_B)*(distancia_A - distancia_B))) / (aceleracion_A - aceleracion_B)


    if tiempo_1 > 0:
      
        punto_interseccion_1 = distancia_A + velocidad_A * tiempo_1 + 0.5 * aceleracion_A * (tiempo_1)**2
        tiempo_3 = punto_interseccion_1/(velocidad_B + aceleracion_B)
        distancia2 = distancia_B + velocidad_B * tiempo_3 + 0.5 * aceleracion_B * tiempo_3**2
        distancia1 = distancia_A + velocidad_B * tiempo_1 + 0.5 * aceleracion_A * tiempo_1 ** 2
        print('''
    El auto A alcanza al auto B a los ''' + str(tiempo_1) + " segundos " + "y a " + str(punto_interseccion_1) + " metros del punto de partida inicial del auto A")
  
    if tiempo_2 > 0:
       # tiempo_3 = distancia_B + velocidad_B * tiempo_2 + 0.5 * aceleracion_B * (tiempo_2**2)
     
        punto_interseccion_1 = distancia_A + velocidad_A * tiempo_2 + 0.5 * aceleracion_A * (tiempo_2)**2
        tiempo_3 = punto_interseccion_1/(velocidad_B + aceleracion_B)
        distancia1 = distancia_A + velocidad_B * tiempo_2 + 0.5 * aceleracion_A * tiempo_2 ** 2
        distancia2 = distancia_B + velocidad_B * tiempo_3 + 0.5 * aceleracion_B * tiempo_3**2
        print("El auto A alcanza al auto B a los " + str(tiempo_2) + " segundos " + "y a " + str(punto_interseccion_1) + " metros del punto de partida inicial del auto A")
 


    print("%s  %s   l    %s  %s  " % (tiempo_1, tiempo_2, punto_interseccion_1, punto_interseccion_2))
    #fig = figure()
    a = arange(10)
    b = arange(10)
    lis2 = [tiempo_3, punto_interseccion_1]
    plot(ecuacioncine(velocidad_A, distancia_A, a, aceleracion_A), color="blue", label="Auto 'A'")
    plot(ecuacioncine(velocidad_B, distancia_B, b, aceleracion_B), color="red", label="Auto 'B'")
   # pit.plot((0, tiempo_3, 0),(punto_interseccion_1, 0, 0), color="red", label="Auto 'B'")
    legend(loc='upper left')
    grid()
    title('Representacion del problema. ')
    xlabel('Tiempo / s')
    ylabel('Punto de interseccion : ' + str(punto_interseccion_1))
 
    show()
#Poner recomendacion de gravedad 9,8 y recibir en string
def FunObjetoCae(Title, peso, gravedad, altura):
    if type(int(peso)) == type(int):
        print("peso : correcto")
    else:
        print("Ingreso de un valor invalido! Reintente!")
    if type(int(gravedad)) == type(int):
        print("gravedad : correcto")
    else:
        print("Ingreso de un valor invalido! Reintente!")
    if type(int(altura)) == type(int):
        print("altura : correcto")
    else:
        print("Ingreso de un valor invalido! Reintente!")
     