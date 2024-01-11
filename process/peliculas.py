from tools.utils import *

#-------------------------------------------

def crear_pelicula():
    lista_pelicula=cargar_json("peliculas.json")
    print("INGRESE LOS DATOS DE LA PELICULA: ")
    id_pelicula=input("ID: ")
    nombre_pelicula=input("Nombre: ")
    duracion=input("Duracion: ")
    sinopsis=input("Sinopsis: ")
    print("INGRESE INFORMACION DE GENEROS: ")
    genero=agregar_cosa("generos.json")
    print("INGRESE INFORMACION DE ACTORES: ")
    actores=agregar_cosa("actores.json")
    print("INGRESE INFORMACION DE FORMATOS: ")
    formato=agregar_cosa("formatos.json")
    
    new_pelicula={    
        "id":id_pelicula,
        "nombre":nombre_pelicula,
        "duracion":duracion,
        "sinopsis":sinopsis,
        "generos":{
            "genero":genero           
        },
        "actores":{
            "actores":actores    
        },
        "formato":{
            "formato":formato
        }         
    }        
        
    lista_pelicula.append(new_pelicula)
    save_json(lista_pelicula,"peliculas.json")
    print("Se ha guardado con exito")

# agrega diccionarios de genero, actores, formato

def agregar_cosa(filename):
    lista_objects=cargar_json(filename)
    nuevo_objeto_agg=[]
    
    id_a_buscar=input("Ingrese id: ")
    
    genero_encontrado=None
    for genero in lista_objects:
        if genero['id']== id_a_buscar:
            genero_encontrado=genero
            break
    
    if not genero_encontrado:
        print("No encontrado")
        return
    
    nuevo_objeto_agg.append(genero_encontrado)
    return nuevo_objeto_agg


#----------------------------------------------------
# Editar pelicula

def editar_pelicula():
    lista_peliculas=cargar_json("peliculas.json")
    id_buscar=input("Ingrese id de la pelicula:")

    pelicula_encotrada=False
    for pelicula in lista_peliculas:
        if pelicula['id']==id_buscar:
            pelicula_encotrada=True
            break
        
    if pelicula_encotrada:
        llave= key_menu(lista_peliculas[0])
        nuevo_valor= input("Ingrese nuevo valor: ")
        
        for pelicula in lista_peliculas:
            if pelicula['id'] == id_buscar:
                pelicula[llave] = nuevo_valor
                break
        
        save_json(lista_peliculas, "peliculas.json")

# imprime las opciones para editar 

def key_menu(dato):
    print("Seleccione una llave:")
    i=0
    for llave in dato.keys():
        i+=1
        print(f"{i}. {llave}")
        
    opcion = int(input("Opción: "))
    if opcion==1:
        respuesta="id"
    elif opcion==2:
        respuesta="nombre"
    elif opcion==3:
        respuesta="apellidos"
    elif opcion==4:
        respuesta="duracion"
    elif opcion==5:
        respuesta="sinopsis"
    elif opcion==6:
        respuesta="generos"
    elif opcion==7:
        respuesta="actores"
    elif opcion==8:
        respuesta="formato"
    else:
        print("No existe")
    return respuesta
    
#-----------------------------------------------------
# buscar pelicula

def buscar_pelicula():
    lista_objects=cargar_json("peliculas.json")
    id_a_buscar=input("Ingrese id de la pelicula: ")
    
    pelicula_encontrado=None
    for pelicula in lista_objects:
        if pelicula['id']== id_a_buscar:
            pelicula_encontrado=pelicula
            break
    
    if not pelicula_encontrado:
        print("No encontrado")
        return
    
    return pelicula


# def modificar(filename):
#     lista_data = cargar_json(filename)
#     id_buscar = int(input("Ingrese numero de identificacion: "))
#     encontrado = False

#     for datos in lista_data:
#         if datos['id'] == id_buscar:
#             encontrado = True
#             break
    
#     if encontrado:
#         llave = key_menu(lista_data[0]) 
#         nuevo_valor = input("Ingrese el nuevo valor: ")

#         for datos in lista_data:
#             if datos["id"] == id_buscar:
#                 datos[llave] = nuevo_valor
#                 break

#         save_json(lista_data, filename)
#     else:
#         print("No se encontro el camper")