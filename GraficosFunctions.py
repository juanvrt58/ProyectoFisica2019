#La linea 2 y 3 se importan las funciones utilizadas en el codigo.
from  pylab import plot, suptitle, xlabel, ylabel, grid, show, arange
from math import radians, sin, sqrt
from matplotlib.pyplot import xlabel
#En las lines 5, 8, 11, 14 Son funciones que contienen las ecuaciones utilizadas. 
def ecuacioncine(v,x, t, a):
    f = x + v * t + 0.5 * a * t**2
    return f
def ecuaciondistancia(v, g):
     d = ((v ** 2) * sin(2 * g)) / 9.8
     return d
def tiempodistancia(v, g):
    t = (2 * v * sin(g))/9.8
    return t
def ybala(angulo, v):
    y = ((v * sin(angulo))**2)/19.6
    return y

# En la linea 19 se encuentra la funcion que grafica el lanzamiento de proyectil.
def FunBala(angulo, velocidad):
    #Se convierte la variable angulo de entero a radianes.
    angulo = radians(angulo)
    # Grafica la funcion de modo que las coordenadas (x, y) en donde x llama a la funcion de tiempo, e 'y' llama a la ecuaciondistancia. Los parametros son velocidad y angulo
    plot((0,  tiempodistancia(velocidad, angulo)), (0, ecuaciondistancia(velocidad, angulo)), color="red")
    #Convierte a una linea de texto una cadena de caracteres.
    lis = ("Altura MAXIMA : %s \nDistancia MAXIMA: %s \nTiempo: %s") % (str(ybala(angulo, velocidad)), str(ecuaciondistancia(velocidad, angulo)), str(tiempodistancia(velocidad, angulo)))
    # Muestra en la parte superior el texto creado a base de la cadena de caracteres en el grafico del proyectil
    suptitle(lis)
    print("Altura maxima que obtiene el proyectil                 : " +  str(ybala(angulo, velocidad)) + " metros")
    print("Distancia maxima que obtiene el proyectil              : " + str(ecuaciondistancia(velocidad, angulo)) + " metros")
    print("Tiempo en que el proyectil llega a la distancia maxima : " + str(tiempodistancia(velocidad, angulo)) + " segundos \n\n") 
    xlabel('Tiempo / s  : ' + str(tiempodistancia(velocidad, angulo)))
    ylabel('Distancia / m : ' + str(ecuaciondistancia(velocidad, angulo)))
    grid() 
    show()   
def FunAutos(velocidad_A, velocidad_B, aceleracion_A, aceleracion_B, distancia_A, distancia_B,):
    tiempo_1, tiempo_2= 0, 0
    punto_interseccion_1, punto_interseccion_2 = 0, 0
    if aceleracion_A != aceleracion_B and velocidad_A != velocidad_B:
        if aceleracion_A == aceleracion_B:
            tiempo_1 = distancia_B / (velocidad_A - velocidad_B)
        elif velocidad_A == velocidad_B:
            tiempo_1 = (sqrt(distancia_B) / (aceleracion_A - aceleracion_B)) 
        else:   
            tiempo_1 = (-(velocidad_A - velocidad_B) + sqrt((velocidad_A - velocidad_B)**2 +(- 4) *0.5*(aceleracion_A - aceleracion_B)*(distancia_A - distancia_B))) / (aceleracion_A - aceleracion_B)
        if aceleracion_A != aceleracion_B:
            punto_interseccion_1 = distancia_B + velocidad_B * tiempo_1 + 0.5 * aceleracion_B * (tiempo_1)**2
        else:
            punto_interseccion_1 = distancia_B + velocidad_B * tiempo_1 + 0.5 * aceleracion_B * (tiempo_1)**2
        if aceleracion_A != aceleracion_B:
            punto_interseccion_1 = distancia_B + velocidad_B * tiempo_1 + 0.5 * aceleracion_B * (tiempo_1)**2
        else:
            punto_interseccion_1 = distancia_B + velocidad_B * tiempo_1 + 0.5 * aceleracion_B * (tiempo_1)**2
        print("El auto A alcanza al auto B a los " + str(tiempo_1) + " segundos " + "y a " + str(punto_interseccion_1) + " metros del punto de partida inicial del auto A")
    else:
        print("Nunca hay tiempo de interseccion!")
        
    plot(ecuacioncine(velocidad_A, distancia_A, arange(10), aceleracion_A), color="blue", label="Auto 'A'")
    plot(ecuacioncine(velocidad_B, distancia_B, arange(10), aceleracion_B), color="red", label="Auto 'B'")

    if aceleracion_A != aceleracion_B and velocidad_A != velocidad_B:
        if punto_interseccion_1 >= 0:
            if punto_interseccion_1 > distancia_B:
                xlabel('No existe punto de interseccion a esta distancia!')
                ylabel("No existe punto de interseccion a esta distancia!")
            else:
                if tiempo_1 >= 0:
                    xlabel('Tiempo / s : ' + str(tiempo_1))
                else: 
                    xlabel('No existe punto de interseccion a esta distancia!')
                if punto_interseccion_1 >= 0:
                    ylabel('Distancia de interseccion : ' + str(punto_interseccion_1))
                else:
                    ylabel("No existe punto de interseccion a esta distancia!")
        else:
            ylabel("En ninguna distancia intersectan los dos autos!")
            xlabel("en ningun tiempo intersectan los dos autos!")
    else:
        ylabel("En ninguna distancia intersectan los dos autos!")
        xlabel("en ningun tiempo intersectan los dos autos!")

    grid()
    show()
