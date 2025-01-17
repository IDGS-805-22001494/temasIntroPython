from io import open

archivo=open("fichero.txt","r")
texto=archivo.readline()
print(texto)
# archivo.seek(0)
print(type(texto))
archivo.close()

# 