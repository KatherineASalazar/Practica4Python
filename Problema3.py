#Crear un programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
#un código que permita hacer un unzip al archivo zipeado.

import zipfile
import os

def zip_image(image_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(image_path, os.path.basename(image_path))

def unzip_file(zip_filename, extract_to):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(extract_to)

def main():
    # Nombre del archivo de la imagen a almacenar y el nombre del archivo ZIP
    image_path = 'C:\Users\Usuario\Desktop\Repositorios\imagen.jpg'
    zip_filename = 'C:\Users\Usuario\Desktop\Repositorios\imagen_zip.zip'

    # Comprimir la imagen en un archivo ZIP
    print(f"Comprimiendo la imagen '{image_path}' como '{zip_filename}'...")
    zip_image(image_path, zip_filename)
    print("Imagen comprimida exitosamente.")

    # Descomprimir el archivo ZIP
    extract_to = 'C:\Users\Usuario\Desktop\Repositorios\unzipped_imagen'
    print(f"Descomprimiendo el archivo ZIP '{zip_filename}'...")
    unzip_file(zip_filename, extract_to)
    print(f"Archivo ZIP descomprimido exitosamente en '{extract_to}'.")

if __name__ == "__main__":
    main()