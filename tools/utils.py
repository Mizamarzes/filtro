import json, os

#-------------------------------------------------------------------------------------------
# cargar json

def cargar_json(filename_path):
    try:
        with open(os.path.join("data", filename_path), 'r') as archivo_json:        
            lista_peliculas = json.load(archivo_json)
            # print("La lista ha sido cargada")
            return lista_peliculas
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []


#---------------------------------------------------------------------------------------------
# guardar json

def save_json(lista_peliculas, filename):
    try:
        with open(os.path.join("data", filename), 'w', encoding="utf-8") as archivo_json:
            json.dump(lista_peliculas, archivo_json, indent=2, ensure_ascii=False)
            # print(f"La lista de {filename} ha sido guardada")
    except FileNotFoundError:
        print(f"El archivo {filename} no existe. Puede que aún no haya peliculas guardados.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {filename}. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido al guardar {filename}: {e}")

#---------------------------------------
# validar opcion y limpiar pantalla

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no esta entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número valido. ")

# limpiar pantalla

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

#-----------------------------------------------
# mostrar json

campo_generos=['id','nombre']
campo_actores=['id','nombre']
campo_formatos=['id','nombre']

def mostrar_listado(nombre_archivo, campos):
    lista_object = cargar_json(nombre_archivo)
    print("Listado: ")
    print("---" * 15)
    
    for dato in lista_object:
        for campo in campos:
            print(f"{campo.capitalize()}: {dato[campo]}")
        print("---" * 15)
