from listasdeCanciones import canciones
from buscarCanciones import buscarCancion
from almacenarNuevasCanciones import almacenarCancion
from editarCancion import editar

print("***biblioteca de canciones***")
print("opcion 1: buscar canciones,  opcion 2: almacenar nueva cancion, opcion 3: editar primera cancion")


def biblioteca(opcion):
  while opcion != 4:
   opcion = int(input("ingrese opcion: "))
   if opcion == 1:
    buscarCancion("")
   elif opcion == 2:
    almacenarCancion(canciones,"")
   elif opcion == 3:
    editar("")
   else: print("vuelva a ingresar la opcion")

biblioteca(int)
    

