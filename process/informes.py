
from tools.utils import *
#------------------------------------------
# listar las peliculas de un genero especifico

def genero_especifico():
    lista_objects=cargar_json("peliculas.json")
    genero_a_buscar=input("Ingrese id del genero a buscar: ")
    
    genero_encontrado=None
    for genero in lista_objects:
        if genero['genero']== genero_a_buscar:
            genero_encontrado=genero
            print(genero_encontrado)
            break
    
    if not genero_encontrado:
        print("No encontrado")
        return

#----------------------------------------------
#buscar pelicula y mostrar la sinopsis y los actores









