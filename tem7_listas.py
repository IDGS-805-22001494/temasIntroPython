lista1=[10,5,3]
lista2=[1,5,2,66,1.70,89,2]
lista3=["lunes","martes","miercoles"]
lista4=["Juan", 45,1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

suma=0
x=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1
    print("la suma es: {}".format(suma)) 
    
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5=[]

for x in range(5):
    valor=int(input("Escribe un numero: "))
    lista5.append(valor)
print(lista5)

# #eliminar elementos de la lista
print(lista1)
lista1.pop()
print(lista1)

'''
Crea un programa donde pida una cantidad n de nuneros y almacernalos en un arreglo la salida
debera ser la siguiente:
listas completas: xxxxxxx
numeros pares: xxxxxxx
numeros impares: xxxxxxx
'''


n = int(input("¿Cuántos números quieres ingresar?: "))
numeros = []
for i in range(n):
    num = int(input("Ingresa un número: "))
    numeros.append(num)
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Lista completa:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)

lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)