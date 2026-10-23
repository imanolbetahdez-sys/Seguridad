import matplotlib.pylab as plt

def abrir(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        # Limpiamos el texto    
        contenido = contenido.lower()
        contenido = contenido.replace(" ", "")
        contenido = contenido.replace("á", "a")
        contenido = contenido.replace("\t", "")
        contenido = contenido.replace("\n", "")
        contenido = contenido.replace("é", "e")
        contenido = contenido.replace("í", "i")
        contenido = contenido.replace("ó", "o")
        contenido = contenido.replace("&", "")

        # Genera una lista con los códigos ASCII de cada carácter
        asciiCodes = [ord(caracter) for caracter in contenido]
        # Retornamos el texto con formato ASCII
        return asciiCodes
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def contarLetras(contenido):
    diccionario = {}
    if contenido is None:
        return None
    for letra in contenido:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

def identificaModa(frecuencias):
    if frecuencias is None:
        return None
    maxFrecuencia = max(frecuencias.values())
    moda = [letra for letra, frecuencia in frecuencias.items() if frecuencia == maxFrecuencia]
    return moda

def convertir(moda):
    if moda is None or len(moda) == 0:
        return None
    letraAscii = ord(chr(moda[0])) if isinstance(moda[0], int) else ord(moda[0])
    return letraAscii

def clave(letraAscii):
    if letraAscii is None:
        return None
    clave_valor = letraAscii - 97
    return clave_valor

if __name__ == "__main__":
    ruta = input("Ingresa el nombre del archivo: ")
    print(abrir(ruta))
    archivo = abrir(ruta)
    frecuencias = contarLetras(archivo)
    print("Frecuencias de letras: ", frecuencias)
    moda = identificaModa(frecuencias)
    print("Letra con mayor frecuencia: ", moda)
    letraAscii = convertir(moda)
    diferenciaLetras = clave(letraAscii)
    print("Diferencia comparada con las letras a: ", diferenciaLetras)
