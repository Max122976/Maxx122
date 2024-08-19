#actividad 5

from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen a marcar: ")
ruta_marca = input("Ingrese la ruta de la marca de agua: ")
ubicacion = input("Ingrese la ubicación de la marca de agua (superior izquierda, superior derecha, inferior izquierda, inferior derecha): ")

with Image.open(ruta_imagen) as imagen, Image.open(ruta_marca) as marca_agua:
    img_width, img_height = imagen.size
    marca_width, marca_height = marca_agua.size
    
    if ubicacion == "superior izquierda":
        posicion = (50, 50)
    elif ubicacion == "superior derecha":
        posicion = (img_width - marca_width - 50, 50)
    elif ubicacion == "inferior izquierda":
        posicion = (50, img_height - marca_height - 50)
    elif ubicacion == "inferior derecha":
        posicion = (img_width - marca_width - 50, img_height - marca_height - 50)
    else:
        print("Ubicación no válida.")
        exit()
    
    imagen.paste(marca_agua, posicion, marca_agua.convert("RGBA"))
    imagen.show()
    
    nuevo_nombre = f"marca_agua_{os.path.basename(ruta_imagen)}"
    imagen.save(nuevo_nombre)
