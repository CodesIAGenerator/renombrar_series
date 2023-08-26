import os
import re

def main():
    # Pide al usuario el directorio donde se encuentran los archivos de la serie
    directorio = input("Por favor, introduce la ruta del directorio donde se encuentran los archivos de la serie: ")

    # Verifica si el directorio es válido
    if not os.path.exists(directorio):
        print("El directorio especificado no existe. Por favor, verifica la ruta e inténtalo de nuevo.")
        return

    # Cambia al directorio especificado
    os.chdir(directorio)

    # Pide al usuario el nombre de la serie
    nombre_serie = input("Introduce el nombre de la serie (por ejemplo, 'La Cupula'): ")

    # Pregunta al usuario el patrón al que desea cambiar
    patron_nuevo = input("Introduce el nuevo patrón (por ejemplo, '1x' para la primera temporada): ")

    # Lista todos los archivos .mkv en el directorio
    archivos = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.mkv')]

    # Lista de expresiones regulares para buscar diferentes patrones
    patrones = [
    re.compile(r'(\d{3})'),  # Formato numérico simple: 101, 102, 103...
    re.compile(r'(\d)x(\d{2})'),  # Temporada y episodio con "x": 1x01, 1x02, 2x01...
    re.compile(r'S(\d{2})E(\d{2})'),  # Temporada y episodio con "S" y "E": S01E01, S01E02, S02E01...
    re.compile(r'T(\d{2})'),  # Temporada con "T": T01, T02, T03...
    re.compile(r'temporada (\d)-(\d{2})'),  # Temporada y episodio con guion: temporada 1-01, temporada 1-02...
    re.compile(r'(\d{3})\d+p'),  # Resolución al final: 101720p, 1021080p, 1034K...
    re.compile(r'(\d{2})-(\d{2})'),  # Formato con guiones: 01-01, 01-02, 02-01...
    re.compile(r'Ep(\d{2})'),  # Formato "Ep": Ep01, Ep02...
    re.compile(r'Episode (\d{2})'),  # Formato "Episode": Episode 01, Episode 02...
    re.compile(r'(\d{4})'),  # Formato numérico extendido: 0101, 0102, 0201...
    re.compile(r'Part (\d{2})'),  # Formato "Part": Part 01, Part 02...
    re.compile(r'(\d{2})of(\d{2})'),  # Formato "of": 01of12, 02of12...
    re.compile(r'(\d{2})_(\d{2})'),  # Formato con guion bajo: 01_01, 01_02, 02_01...
    re.compile(r'(\d{2})\.(\d{2})'),  # Formato con punto: 01.01, 01.02, 02.01...
    re.compile(r'(\d{2})\s(\d{2})')  # Formato con espacio: 01 01, 01 02, 02 01...
    ]


    for archivo in archivos:
        encontrado = False
        for regex in patrones:
            coincidencia = regex.search(archivo)
            if coincidencia:
                # Extrae el número del patrón
                numero = coincidencia.group(1)
                # Crea el nuevo nombre del archivo usando el nuevo patrón
                nuevo_nombre = f"{nombre_serie} {patron_nuevo}{int(numero[-2:]):02}.mkv"
                os.rename(archivo, nuevo_nombre)
                print(f"'{archivo}' renombrado a '{nuevo_nombre}'")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró ningún patrón en: {archivo}")

if __name__ == "__main__":
    main()
