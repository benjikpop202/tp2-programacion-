#from listasdeCanciones import canciones
def almacenarCancion(canciones,almacenar):
 while 1:
  almacenar = input("ingrese nueva cancion: ")
  canciones.append(almacenar)
  arista = input("ingrese artista: ")
  letra = input("ingrese letra: ")
  cancion6 = {"nombre":almacenar,"artista":arista,"letra":letra}
  print("nombre: ",almacenar," artista: ",arista," letra: ",letra)
  print("almacenado con exito!!")
  

       