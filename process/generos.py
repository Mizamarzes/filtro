from tools.utils import *

#-------------------------------------------
# crear genero

def crear_genero():
    lista_generos=cargar_json("generos.json")
    id_genero=input("Ingrese la id del genero: ")
    nombre_genero=input("Ingrese el nombre del genero: ")
    
    new_genero={
        "id": id_genero,
        "nombre": nombre_genero
    }
    
    lista_generos.append(new_genero)
    save_json(lista_generos,"generos.json")
    print("Se ha guardado con exito")
    
















