import argparse
from PIL import Image
import os

def redimensionar_imagenes(carpeta_original, tamaños):
    # Redimensionar cada imagen
    for nombre_archivo in os.listdir(carpeta_original):
        if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_original = os.path.join(carpeta_original, nombre_archivo)
            with Image.open(ruta_original) as img:
                # Guardar cada versión redimensionada
                for tamaño_nombre, tamaño in tamaños.items():
                    img_redimensionada = img.copy()
                    img_redimensionada.thumbnail(tamaño)  # Mantiene la proporción
                    # Agregar el nombre del tamaño al nombre del archivo
                    nombre_salida = f"{os.path.splitext(nombre_archivo)[0]}_{tamaño_nombre}.jpg"
                    ruta_salida = os.path.join(carpeta_original, nombre_salida)
                    img_redimensionada.save(ruta_salida, "JPEG", quality=85)
                    print(f"Guardada {ruta_salida}")

# Definir tamaños deseados en píxeles (ejemplo: thumbnails y web)
tamaños = {
    'thumbnail': (150, 150),
    'web': (800, 800),
}

# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description="Redimensionar imágenes en una carpeta")
parser.add_argument('--path', required=True, help="Ruta de la carpeta con las imágenes originales")

# Parsear argumentos
args = parser.parse_args()

# Carpeta de origen
carpeta_original = args.path

# Ejecutar función de redimensionamiento
redimensionar_imagenes(carpeta_original, tamaños)