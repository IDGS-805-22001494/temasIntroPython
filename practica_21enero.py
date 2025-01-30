import os
from datetime import datetime

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.boletos = 0
        self.total_pagado = 0
        self.descuento_total = 0

class SistemaCine:
    def __init__(self):
        self.PRECIO_BOLETO = 12
        self.compradores = []
        self.archivo_registro = "registro_compras.txt"
        self.total_boletos_vendidos = 0
        self.total_recaudado = 0
        self.total_descuentos = 0

    def registrar_compra(self, comprador, cantidad_boletos, tiene_cineco):
        precio_final, descuento = self._calcular_precio(cantidad_boletos, tiene_cineco)
        comprador.boletos += cantidad_boletos
        comprador.total_pagado += precio_final
        comprador.descuento_total += descuento
        self.total_boletos_vendidos += cantidad_boletos
        self.total_recaudado += precio_final
        self.total_descuentos += descuento
        self._mostrar_en_terminal(comprador, cantidad_boletos, precio_final, descuento, tiene_cineco)

    def _calcular_precio(self, cantidad_boletos, tiene_cineco):
        precio_base = cantidad_boletos * self.PRECIO_BOLETO
        
        if cantidad_boletos > 5:
            descuento = 0.15
        elif cantidad_boletos >= 3:
            descuento = 0.10
        else:
            descuento = 0
            
        descuento_cantidad = precio_base * descuento
        precio_con_descuento = precio_base - descuento_cantidad
        
        if tiene_cineco:
            descuento_cineco = precio_con_descuento * 0.10
            precio_final = precio_con_descuento - descuento_cineco
            descuento_total = descuento_cantidad + descuento_cineco
        else:
            precio_final = precio_con_descuento
            descuento_total = descuento_cantidad
            
        return precio_final, descuento_total

    def _mostrar_en_terminal(self, comprador, cantidad_boletos, precio_final, descuento, tiene_cineco):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n=== Resumen de Compra ===")
        print(f"Nombre: {comprador.nombre}")
        print(f"Boletos comprados: {cantidad_boletos}")
        print(f"Total pagado: ${precio_final:,.0f}")
        print(f"Descuento aplicado: ${descuento:,.0f}")
        print(f"Tarjeta CINECO: {'Sí' if tiene_cineco else 'No'}")
        print(f"Fecha y hora: {timestamp}")
        print("=========================\n")

    def guardar_ventas_en_archivo(self):
        with open(self.archivo_registro, "w") as f:
            # f.write("=== Registro de Compras ===\n")
            for comprador in self.compradores:
                f.write(f"\nNombre: {comprador.nombre}\n")
                # f.write(f"Boletos comprados: {comprador.boletos}\n")
                f.write(f"Total pagado: ${comprador.total_pagado:,.0f}\n")
                # f.write(f"Descuento aplicado: ${comprador.descuento_total:,.0f}\n")
            f.write("\n=== Resumen Final ===\n")
            # f.write(f"Total de boletos vendidos: {self.total_boletos_vendidos}\n")
            f.write(f"Total recaudado: ${self.total_recaudado:,.0f}\n")
            # f.write(f"Total de descuentos aplicados: ${self.total_descuentos:,.0f}\n")

    def mostrar_resumen_final(self):
        print("\n=== Resumen Final de Compras ===")
        for comprador in self.compradores:
            print(f"\nComprador: {comprador.nombre}")
            print(f"Total de boletos: {comprador.boletos}")
            print(f"Total pagado: ${comprador.total_pagado:,.0f}")
            print(f"Total de descuentos: ${comprador.descuento_total:,.0f}")
        print("\n=== Totales ===")
        print(f"Total de boletos vendidos: {self.total_boletos_vendidos}")
        print(f"Total recaudado: ${self.total_recaudado:,.0f}")
        print(f"Total de descuentos aplicados: ${self.total_descuentos:,.0f}")

def main():
    sistema = SistemaCine()
    
    while True:
        nombre = input("\nIngrese el nombre del comprador: ")
        comprador = Persona(nombre)
        sistema.compradores.append(comprador)
        
        while True:
            try:
                num_personas = int(input("¿Cuántas personas son? "))
                if num_personas <= 0:
                    print("La cantidad de personas debe ser un número positivo.")
                    continue

                num_boletos = int(input("¿Cuántos boletos desea comprar? "))
                max_boletos = num_personas * 7

                if num_boletos > max_boletos:
                    print(f"¡Alerta! No puede comprar más de {max_boletos} boletos para {num_personas} personas.")
                    while True:
                        print("\nOpciones:")
                        print("1. Cambiar la cantidad de boletos.")
                        print("2. Agregar más personas.")
                        opcion = input("Seleccione una opción (1/2): ")
                        
                        if opcion == '1':
                            num_boletos = int(input(f"Ingrese la nueva cantidad de boletos (máximo {max_boletos}): "))
                            if num_boletos > max_boletos:
                                print(f"Cantidad no válida. Se establecerá en {max_boletos} boletos.")
                                num_boletos = max_boletos
                            break
                        elif opcion == '2':
                            num_personas = int(input("Ingrese la nueva cantidad de personas: "))
                            max_boletos = num_personas * 7
                            num_boletos = int(input(f"Ingrese la cantidad de boletos (máximo {max_boletos}): "))
                            if num_boletos > max_boletos:
                                print(f"Cantidad no válida. Se establecerá en {max_boletos} boletos.")
                                num_boletos = max_boletos
                            break
                        else:
                            print("Opción no válida. Intente de nuevo.")
                
                tiene_cineco = input("¿Tiene tarjeta CINECO? (s/n): ").lower()
                if tiene_cineco not in ['s', 'n']:
                    print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")
                    continue
                tiene_cineco = tiene_cineco == 's'

                sistema.registrar_compra(comprador, num_boletos, tiene_cineco)
                break
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        continuar = input("\n¿Desea registrar otra compra? (s/n): ").lower()
        if continuar != 's':
            break
    
    sistema.mostrar_resumen_final()
    sistema.guardar_ventas_en_archivo()
    print("\nEl registro completo de compras se ha guardado en:", sistema.archivo_registro)

if __name__ == "__main__":
    main()