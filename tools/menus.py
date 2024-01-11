from tools.utils import *

#-------------------------------------
# Menu principal

def menu_principal():
    print("-------SISTEMA GESTOR DE PELICULAS BLOCKBUSTER------")
    print("1. Administrador de Generos")
    print("2. Administrador de Actores")
    print("3. Administrador de Formatos")
    print("4. Gestor de Informes")
    print("5. Gestor de peliculas")
    print("6. Salir")
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_generos():
    print("----GESTOR DE GENEROS-----")
    print("1. Crear genero")
    print("2. Listar generos")
    print("3. Ir al Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_actores():
    print("-----GESTOR DE ACTORES----")
    print("1. Crear Actor")
    print("2. Listar Actor")
    print("3. Ir al Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_formatos():
    print("-----GESTOR DE FORMATOS--------")
    print("1. Crear formatos")
    print("2. Listar formatos")
    print("3. Ir al Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_peliculas():
    print("------GESTOR DE PELICULAS------")
    print("1. Agregar pelicula")
    print("2. Editar pelicula")
    print("3. Eliminar pelicula")
    print("4. Eliminar Actor")
    print("5. Buscar pelicula")
    print("6. Listar todas peliculas")
    print("7. Ir al Menu Principal")
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_informes():
    print("----- GESTOR DE INFORMES---------")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Listar las peliculas donde el protagonista sea Silvester Stallone")
    print("3. Buscar pelicula y mostrar sinopsis y los actores")
    print("4. Ir al Menu principal")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    