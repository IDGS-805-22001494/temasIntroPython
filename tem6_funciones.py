import os

def funcion1():
    os.system("cls")
    print("hola, soy funcion1")
    num1=int(input("numero1:  "))
    num2=int(input("numero2:  "))
    res=num1+num2
def funcion2():
    print("hola, soy funcion2")


def run():
    os.system("cls")
    print("menu opciones")
    print("1: funcion1")
    print("2: funcion2")
    print("0: salir")
    opcion=int(input("opcion:  "))
    if opcion==1:
        funcion1()
    if opcion==2:
        funcion2()
if __name__=="__main__":
    run()

op=int(input("numeros:  "))
if op==1:
    funcion1()
else:
    funcion2()
