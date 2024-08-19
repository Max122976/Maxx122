#actividad 2

from PIL import Image

ruta_imagen = input("Ingrese la ruta de la imagen: ")
nuevo_nombre = input("Ingrese el nuevo nombre para la imagen (con extensión, ej. nueva_imagen.png): ")

with Image.open(ruta_imagen) as img:
    img.show()
    img.save(nuevo_nombre)
