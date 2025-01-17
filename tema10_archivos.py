from io import open

texto='Una linea de texto en un archivo\nOtra linea de texto en el mismo archivo\nY otra mas\n'

fichero=open("fichero.txt","w")
fichero.write(texto)

cadena2="Esto es una cadena"
fichero.write(cadena2)

cadena3="Esto es otra cadena 3"
fichero.write(cadena3)
fichero.close()