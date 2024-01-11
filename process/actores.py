from tools.utils import *

#---------------------------------------
# crear actor 

def crear_actor():
    lista_actores=cargar_json("actores.json")
    id_actor=input("Ingrese la id del actor: ")
    nombre_actor=input("Ingrese el nombre del actor: ")
    
    new_actor={
        "id": id_actor,
        "nombre": nombre_actor
    }
    
    lista_actores.append(new_actor)
    save_json(lista_actores,"actores.json")
    print("Se ha guardado con exito")
    
