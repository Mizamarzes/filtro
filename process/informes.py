
from tools.utils import *
#------------------------------------------
# listar las peliculas de un genero especifico

def genero_especifico():
    lista_objects=cargar_json("peliculas.json")
    genero_a_buscar=input("Ingrese id del genero a buscar: ")
    peliculas_del_genero=[]
    
    for pelicula in lista_objects:
        if genero_a_buscar in pelicula['generos'].lower():
            peliculas_del_genero.append(pelicula)
    
    if peliculas_del_genero:
        print(f"Películas del género '{genero_a_buscar}':")
        for pelicula in peliculas_del_genero:
            print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}")
    else:
        print(f"No hay películas del género '{genero_a_buscar}'.")

#----------------------------------------------
#buscar pelicula y mostrar la sinopsis y los actores









