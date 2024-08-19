#Actividad 4

from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")
x = int(input("Ingrese la coordenada X del recorte: "))
y = int(input("Ingrese la coordenada Y del recorte: "))
ancho = int(input("Ingrese el ancho del recorte: "))
altura = int(input("Ingrese la altura del recorte: "))

with Image.open(ruta_imagen) as img:
    if (x < 0 or y < 0 or x + ancho > img.width or y + altura > img.height):
        print("Parámetros no válidos.")
    else:
        area_recorte = (x, y, x + ancho, y + altura)
        img_recortada = img.crop(area_recorte)
        img_recortada.show()
        
        if not os.path.exists('recortes'):
            os.makedirs('recortes')
        
        num_recortes = len(os.listdir('recortes'))
        nuevo_nombre = f"recortes/recorte{num_recortes + 1}.png"
        img_recortada.save(nuevo_nombre)
