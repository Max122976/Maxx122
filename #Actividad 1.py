#Actividad 1
from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")

with Image.open(ruta_imagen) as img:
    nombre, extension = os.path.splitext(os.path.basename(ruta_imagen))
    resolucion = img.size
    cantidad_pixeles = resolucion[0] * resolucion[1]
    
    img.show()
    
    print(f"{'Nombre':<15} {'Extensión':<10} {'Resolución':<15} {'Píxeles':<10} {'Ubicación'}")
    print(f"{nombre:<15} {extension:<10} {resolucion[0]}x{resolucion[1]:<15} {cantidad_pixeles:<10} {ruta_imagen}")

