from listasdeCanciones import cancion1
def editar(datosCambiar):
   while 1:
    datosCambiar = input("los datos actuales son: nombre: " + cancion1["nombre"]+","
    " artista: "+ cancion1["artista"]+"," "letra: "+ cancion1["letra"]+"," " que valor quieres cambiar?: ")
    valorNuevo = input("ingrse nuevo valor: ")
    if (valorNuevo == cancion1["nombre"]):
      print("dato ya almacenado, ingrese uno nuevo")
    elif valorNuevo == cancion1["artista"]:
      print("dato ya almacenado, ingrese uno nuevo")
    elif valorNuevo == cancion1["letra"]:
      print("dato ya almacenado, ingrese uno nuevo")
    else:
     cancion1[datosCambiar] = valorNuevo 

  

   
