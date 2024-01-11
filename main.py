# El proyecto trata sobre un tema cinematografico de peliculas
# se debe poder crear, editar y eliminar peliculas, brindando un control total sobre la base de datos
# funcionalidad de busqueda, se requiere opciones para buscar peliculas tanto por genero como por el codigo unico asignado

from tools.menus import *
from tools.utils import *
from process.generos import crear_genero
from process.actores import crear_actor
from process.formatos import crear_formato
from process.peliculas import *
from process.informes import *

def generos():
    while True:
        limpiar_pantalla()
        subopcion=menu_generos()
        if subopcion==1:
            crear_genero()
        elif subopcion==2:
            mostrar_listado("generos.json", campo_generos)
            input("[Presione cualquier tecla para continuar]: ")
        elif subopcion==3:
            break

def actores():
    while True:
        limpiar_pantalla()
        subopcion = menu_actores()
        if subopcion == 1:
            crear_actor()
        elif subopcion == 2:
            mostrar_listado("actores.json", campo_actores)
            input("[Presione cualquier tecla para continuar]: ")
        elif subopcion == 3:
            break


def formatos():
    while True:
        limpiar_pantalla()
        subopcion=menu_formatos()
        if subopcion==1:
            crear_formato()
        elif subopcion==2:
            mostrar_listado("formatos.json", campo_formatos)
            input("[Presione cualquier tecla para continuar]: ")
        elif subopcion==3:
            break

def informes():
    while True:
        limpiar_pantalla()
        subopcion=menu_informes()
        if subopcion==1:
            print()
        elif subopcion==2:
            print()
        elif subopcion==3:
            print()
        elif subopcion==4:
            break

def peliculas():
    while True:
        limpiar_pantalla()
        subopcion=menu_peliculas()
        if subopcion==1:
            crear_pelicula()
        elif subopcion==2:
            editar_pelicula()
        elif subopcion==3:
            print()
        elif subopcion==4:
            print()
        elif subopcion==5:
            pelicula=buscar_pelicula
        elif subopcion==6:
            print()
        elif subopcion==7:
            break
            
#-------------------------------------------------------
# control principal 

while True:
    limpiar_pantalla()
    opcion=menu_principal()
    if opcion==1:
        generos()
    elif opcion==2:
        actores()
    elif opcion==3:
        formatos()
    elif opcion==4:
        informes()
    elif opcion==5:
        peliculas()
    elif opcion==6:
        print("Saliendoo...")
        break