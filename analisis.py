#programa para contar frecuencias de palabras en texto

import matplotlib.pylab as plt
def leerArchivo(nombreArchivo):
    with open(nombreArchivo, "r") as archivo :
        contenido = archivo.read()
    
    contenidoLimpio = contenido.lower()
    contenidoLimpio = contenidoLimpio.replace(" ","")
    contenidoLimpio = contenidoLimpio.replace("á","a")
    contenidoLimpio = contenidoLimpio.replace("\t","")
    contenidoLimpio = contenidoLimpio.replace("\n","")
    contenidoLimpio = contenidoLimpio.replace("é","e")
    contenidoLimpio = contenidoLimpio.replace("í","i")
    contenidoLimpio = contenidoLimpio.replace("ó","o")
    contenidoLimpio = contenidoLimpio.replace("&","")


    return contenidoLimpio

def contarLetras(contenidoLimpio):
    diccionario={}
    if contenidoLimpio is None:
        return None
    for letra in contenidoLimpio:
        if letra in diccionario:
            diccionario[letra]+=1
        else:
            diccionario[letra]=1
    return diccionario
    
def graficarFrecuencias(frecuencias):
    if frecuencias is None:
        return 
    caracteres = list(frecuencias.keys())
    valores = list(frecuencias.values())
    plt.bar(caracteres, valores)
    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencias')
    plt.title('Frecuencias de caracteres')
    plt.show()

def identificaModa(frecuencias):
    if frecuencias is None:
        return None
    maxFrecuencia = max(frecuencias.values())
    moda = [letra for letra, frecuencia in frecuencias.items() if frecuencia == maxFrecuencia]
    return moda

if __name__ == "__main__":
    nombreArchivo = input("Ingresa el nombre del archivo: ")
    print(leerArchivo(nombreArchivo))
    archivo = leerArchivo(nombreArchivo)
    frecuencias = contarLetras(archivo)
    print("Frecuencias de letras: ", frecuencias)
    graficarFrecuencias(frecuencias)
    moda = identificaModa(frecuencias)
    print("Letra con mayor frecuencia: ", moda)
