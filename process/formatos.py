from tools.utils import *

#---------------------------------------
# crear formato

def crear_formato():
    lista_formatos=cargar_json("formatos.json")
    id_formato=input("Ingrese la id del formato: ")
    nombre_formato=input("Ingrese el nombre del formato: ")
    
    new_formato={
        "id": id_formato,
        "nombre": nombre_formato
    }
    
    lista_formatos.append(new_formato)
    save_json(lista_formatos,"formatos.json")
    print("Se ha guardado con exito")
    
