#  Cree un programa el cual cumpla con las siguientes especificaciones:
#- Solicite al usuario el nombre de una fuente a utilizar. En caso no se ingrese ninguna
#  fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
#- Solicite al usuario un texto.
#- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
#  apropiada.
#Notas:
#- Instalar la librería usando: pip install pyfiglet
#- Para usar la librería, debe hacer:
#from pyfiglet import Figlet
#figlet = Figlet()
#- Puede obtener la lista de fuentes disponibles usando: figlet.getFonts()
#- Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada)
#- Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir))
#- Recuerde que random tiene un método random choice

import os
from pyfiglet import Figlet

import random

def select_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    while True:
        font_choice = input("Ingrese el nombre de la fuente a utilizar o presione Enter para seleccionar una fuente aleatoria:\n")
        if font_choice == "":
            return random.choice(fonts)
        elif font_choice in fonts:
            return font_choice
        else:
            print("La fuente ingresada no es válida. Por favor, elija una fuente de la lista.")

def main():
    font = select_font()
    figlet = Figlet(font=font)
    user_text = input("Ingrese el texto a imprimir:\n")
    rendered_text = figlet.renderText(user_text)
    print(rendered_text)

if __name__ == "__main__":
    main()