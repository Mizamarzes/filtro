
from tools.utils import *
#------------------------------------------
# listar las peliculas de un genero especifico

def genero_especifico():
    lista_objects=cargar_json("peliculas.json")
    genero_a_buscar=input("Ingrese id del genero a buscar: ")
    
    for pelicula in lista_objects:
        generos_pelicula = pelicula.get('generos', [])
        for genero_lista in generos_pelicula:
            for genero in genero_lista:
                if genero['id'] == genero_a_buscar:
                    print(pelicula)
                    break
    
#-------------------------------------------------------------
# peliculas donde sea el mismo protagonista

def peliculas_protagonista():
    lista_objects=cargar_json("peliculas.json")
    protagonista_a_buscar=input("Ingrese id del protagonista a buscar: ")
    
    for pelicula in lista_objects:
        actores_pelicula = pelicula.get('actores', [])
        for actor_lista in actores_pelicula:
            for actor in actor_lista:
                if actor['id'] == protagonista_a_buscar:
                    print(pelicula)
                    break 
                
#----------------------------------------------
#buscar pelicula y mostrar la sinopsis y los actores

def buscar_peli_sinopsis_actores():
    lista_objects=cargar_json("peliculas.json")
    pelicula_a_buscar=input("Ingrese id de la pelicula a buscar: ")
    
    for pelicula in lista_objects:
        if pelicula['id']==pelicula_a_buscar:
            print(f"Sinopsis de la pelicula: {pelicula['sinopsis']}")
            print(f"Actores de la pelicula: {pelicula['actores']}")
    





