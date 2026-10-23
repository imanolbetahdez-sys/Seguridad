def encriptar(texto, clave):
    resultado =""
    claveRepetida = (clave * (len(texto) // len(clave)+1))[:len(texto)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            desplazamiento = ord(claveRepetida[i].lower()) - ord('a')
            if texto[i].isupper():
                resultado +=chr((ord(texto[i])-ord('A')+desplazamiento)%26 +ord('A'))
            else:
                resultado +=chr((ord(texto[i])-ord('a')+desplazamiento)%26 +ord('a'))
        else:
            resultado +=  texto[i]
    return resultado

def desencriptar(mensaje, clave):
    resultado = ""
    claveRepetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]
    for i in range(len(mensaje)):
        if mensaje[i].isalpha():
            desplazamiento = ord(claveRepetida[i].lower()) - ord('a')
            if mensaje[i].isupper():
                resultado += chr((ord(mensaje[i]) - ord('A') - desplazamiento) % 26 + ord('A'))
            else:
                resultado += chr((ord(mensaje[i]) - ord('a') - desplazamiento) % 26 + ord('a'))
        else:
            resultado += mensaje[i]
    return resultado

if __name__ == "__main__":
    while true:
        print("Elige lo que quieres hacer")
        print("--------------------------")
        print("1.- Encriptar ")
        print("2.- Desencriptar ")
        print("3.- salir ")
        print("--------------------------")
        opcion = input("Elige uno entre el 1 y 3 \n")
        if(opcion == "1"):
            mensaje = input("Dame el mensaje a encriptar: ")
            clave = input("Dame la clave de encriptamiento: ")
            mensajeEncriptado=encriptar(mensaje, clave)
            print(mensajeEncriptado)
        elif(opcion == "2"):
            mensaje = input("Dame el mensaje a desencriptar: ")
            clave = input("Dame la clave de encriptamiento: ")
            mensajeDesencriptado=desencriptar(mensaje, clave)
            print(mensajeDesencriptado)
        elif(opcion == "3"):
            break
        else:
            print("Opcion no valida ingresa una opcion entre 1 y 3")