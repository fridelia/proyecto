# poner un def, para acortar codigo..regresar a input de archivo, o menú general
import os #checar equivalente
import platform
import shutil
from pathlib import Path

#Variables utilizadas en todos los ciclos y funciones
current_directory = Path.cwd()
path = Path(current_directory) 

##Función para validar existencia de archivos (problema con esta función)
def validar(ruta_archivo):
    
    data = input(ruta_archivo)
    path_folder = path / data
    
    if path_folder.exists():
        return True
    else:
        print('error, nombre incorrecto')
        return False
        #except ValueError:
        #   print("El dato ")


#Función Listar
def listar():
    for dir in path.iterdir():
        if dir.is_file() and dir.suffix == '.txt':
            print(dir.name)

#Función leer
def leer():
    path_file2 = path / eleccionLeer
    if path_file2.exists():
        #print("ok)")
        with open(path_file2, 'r') as file:
            content = file.read()
        #content = path_file2.read_text()
            print(content)

#Función Editar
def editar():
    path_file = path / eleccionFileEd
    if path_file.exists() and eleccionEditar == "1":
        with open(path_file, 'w') as file:
            file.write(nuevo_tex)
    elif path_file.exists() and eleccionEditar == "2":
        with open(path_file, 'a') as file:
            file.write(nuevo_tex)

#Función eliminar
def eliminar():
    path_file = path / eleccionEliminar
    path_file.unlink()


#Menú principal
cicloMenu1 = True
while cicloMenu1:
    print("\nMenú principal")
    print("1. Listar archivos")
    print("2. Leer archivo")
    print("3. Editar archivo")
    print("4. Eliminar archivo")
    print("5. Limpiar consola") #Se incorporó la sugerencia de añadir esta función de la asesoría #1 sobre un proyecto de este tipo.
    print("6. Salir")


    opcionMenu = input("Ingrese una opción con número: ") #validar que sea número

#Cada elección en if else llama a una función
    if opcionMenu == "1":
        listar()

    elif opcionMenu == "2":
        mensajeLeer = "Elija el archivo que desea leer de la lista: "
        print(mensajeLeer)
        listar()

        cicloValidar1 = True
        while True:
            eleccionLeer = (input("\nsu elección: ")) #validar nombre
            if validar(eleccionLeer):
                leer()
                cicloValidar1 = False
            #if eleccionLeer.is_file():
                #print('se puede leer')
                #cicloValidar1 = False
            else:
                cicloValidar1 = False
                #print('error, intenta de nuevo')
            

    elif opcionMenu == "3":
        print("Ingrese el archivo que desea editar")
        listar()
        eleccionFileEd = input("\nsu elección: ")

#Se añadió un segundo ciclo While dentro del Ciclo del Menú principal para mostrar las opciones de edición, así como retornar al menú ppal.
        cicloMenu2 = True
        while cicloMenu2:
            mensajeEditar = ("Menú módulo editar \nElija el tipo de edición que desea ejecutar: ")
            print(mensajeEditar, "\n1. Sobreescribir en el archivo \n2. Añadir texto al final del contenido \n3. Regresar al menú principal")
            eleccionEditar= input("\nsu elección: ")

            if eleccionEditar == "1" or eleccionEditar == "2": 
                nuevo_tex = input("Escriba el texto a añadir: ")
                editar()
                cicloMenu2 = False
            elif eleccionEditar == "3":
                cicloMenu2 = False
            else:
                print("Selecciona solo números del 1 al 3, intenta de nuevo\n")


    elif opcionMenu == "4":
        print("Ingrese el archivo que desea eliminar")
        listar()
        eleccionEliminar = input("\nsu elección: ")
        eliminar()

    elif opcionMenu == "5":
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    elif opcionMenu == "6":
        cicloMenu1 = False  

    else:
        print("Selecciona solo números del 1 al 5, intenta de nuevo\n")



#añadir .txt a concatenar para eliminar la necesidad de escribirla
#reconocer nombre del archivo tanto con minúsculas como mayúsculas
#cambiar menu2 a submenu




