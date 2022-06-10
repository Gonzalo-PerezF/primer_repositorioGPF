#Jugador de futbol
#Datos de entrada de mi programa

#Diccionario sin datos
jugador = {}

jugador["Nombre"] = input("Nombre del jugador:???\n")

jugador["Apellido"] =  input("Apellido del jugador:???\n")

jugador["Edad"] = int (  input("Edad del jugador:???\n") )

jugador["Precio"] = float (  input("Precio del jugador:???\n") )


for clave in jugador:


    print(f"{clave} ------> {jugador[clave]}")