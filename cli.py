import shutil
from pathlib import Path

#Variables utilizadas en todos los ciclos y funciones
directorio_actual = Path.cwd()
ruta = Path(directorio_actual)

#Función Listar
def listar():
    for dir in ruta.iterdir():
        if dir.is_file() and dir.suffix == '.txt':
            print(dir.name)

#Función leer
def leer():
    with open(ruta_leer, 'r') as file:
        contenido = file.read()
        print(contenido)

#Función Editar
def editar():
    ruta_editar = ruta / eleccionFileEd
    if ruta_editar.exists() and eleccionEditar == "1":
        with open(ruta_editar, 'w') as file:
            file.write(nuevo_tex)
    elif ruta_editar.exists() and eleccionEditar == "2":
        with open(ruta_editar, 'a') as file:
            file.write(nuevo_tex)

#Función eliminar
def eliminar():
    ruta_eliminar = ruta / eleccionEliminar
    ruta_eliminar.unlink()


#Menú principal
Menuppal = True
while Menuppal:
    print("\nMenú principal")
    print("1. Listar archivos")
    print("2. Leer archivo")
    print("3. Editar archivo")
    print("4. Eliminar archivo")
    print("5. Salir")


    opcionMenu = input("\nIngrese un número como opción: ") #validar que sea número
    
#Cada elección en if else llama a una función
    if opcionMenu == "1":
        listar()

    elif opcionMenu == "2":
        print("\nElija el archivo que desea leer de la lista: ")
        listar()
        eleccionLeer = input("\nSu elección: ") #validar nombre
        ruta_leer = ruta /eleccionLeer
        if ruta_leer.exists():
            leer()
        else:
            print('Nombre del archivo incorrecto, intente de nuevo.')
        
        
    elif opcionMenu == "3":
        print("Ingrese el archivo que desea editar")
        listar()
        
        eleccionFileEd = input("\nsu elección: ")
        ruta_editar = ruta / eleccionFileEd
        if ruta_editar.exists():

#Se añadió un segundo ciclo While dentro del Ciclo del Menú principal para mostrar las opciones de edición, así como retornar al menú ppal.
            SubmenuEd = True
            while SubmenuEd:
                mensajeEditar = ("\nSubmenú módulo editar \nElija el tipo de edición que desea ejecutar: ")
                print(mensajeEditar, "\n1. Sobreescribir en el archivo \n2. Añadir texto al final del contenido \n3. Regresar al menú principal")
                eleccionEditar= input("\n \nSu elección: ")

                if eleccionEditar == "1" or eleccionEditar == "2": 
                    nuevo_tex = input("Escriba el texto a añadir: ")
                    editar()
                    SubmenuEd = False
                elif eleccionEditar == "3":
                    SubmenuEd = False
                else:
                    print("Selecciona solo números del 1 al 3, intenta de nuevo\n")
        
        else:
            print("Nombre del archivo, intente de nuevo.")

    elif opcionMenu == "4":
        print("\nIngrese el archivo que desea eliminar")
        listar()
        eleccionEliminar = input("\nSu elección: ")
        eliminar()

    elif opcionMenu == "5":
        Menuppal = False  

    else:
        print("Selecciona solo números del 1 al 5, intenta de nuevo\n")