from listasdeCanciones import cancion1, cancion2, cancion3, cancion4, cancion5
def buscarCancion(Cancion):
  while 1:
     Cancion = input("ingrese cancion: ")
     if Cancion == "despacito":
      print("nombre: ",cancion1["nombre"]," artista: ",cancion1["artista"]," letra: ",cancion1["letra"])
     elif Cancion == "sorry":
      print("nombre: ",cancion2["nombre"]," artista: ",cancion2["artista"]," letra: ",cancion2["letra"])
     elif Cancion == "butter":
      print("nombre: ",cancion3["nombre"]," artista: ",cancion3["artista"]," letra: ",cancion3["letra"])
     elif Cancion == "titanium":
      print("nombre: ",cancion4["nombre"]," artista: ",cancion4["artista"]," letra: ",cancion4["letra"])
     elif Cancion == "limbo":
      print("nombre: ",cancion5["nombre"]," artista: ",cancion5["artista"]," letra: ",cancion5["letra"])
     else: print("cancion no registrada")

