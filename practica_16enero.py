'''Calcular la distancia entre dos puntos en el espacio 
    los puntos en el plano los eligira el usuario
'''

import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )

def main():
    print("Ingrese las coordenadas del primer punto:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("Ingrese las coordenadas del segundo punto:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    distancia = calcular_distancia(x1, y1,x2, y2 )
    print(f"La distancia entre los dos puntos es: {distancia}")

if __name__ == "__main__":
    main()
    
