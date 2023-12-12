# script.py

import os
from subprocess import run

def extract_translations():
    run(["pybabel", "extract", "-F", "babel.cfg", "-o", "messages.pot", "."])

def initialize_translation(locale):
    run(["pybabel", "init", "-i", "messages.pot", "-d", "translations", "-l", locale])

def compile_translations():
    run(["pybabel", "compile", "-d", "translations"])

def update_translations():
    run(["pybabel", "update", "-i", "messages.pot", "-d", "translations"])

def main():
    # Extraer cadenas para traducción
    extract_translations()

    # Inicializar traducciones para el idioma español
    initialize_translation("es")

    # Compilar traducciones
    compile_translations()

    # Actualizar traducciones (opcional, según sea necesario)
    # update_translations()

if __name__ == "__main__":
    main()
