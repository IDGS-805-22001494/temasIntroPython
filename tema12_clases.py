class OperasBas:
    # declaracion de propiedades
    num1 = 0
    num2 = 0
    res=0
    # deeclaracion del constructor de la clase
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b    
    # delcaracion de los metodos de la clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: ",self.res)
        
def main():
    obj=OperasBas(10,20)
    obj.suma()
    
    
    
    

if __name__ == "__main__":
        main()    