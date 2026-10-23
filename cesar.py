def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Solo ciframos letras
            # Determinar si es mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            # Aplicar el desplazamiento con módulo 26
            nuevo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo)
        else:
            # Si no es letra, se deja igual
            resultado += caracter
    return resultado

# Ejemplo de uso
texto = input("Ingresa el texto")
clave = 3  # Desplazamiento de 3 posiciones
cifrado = cifrado_cesar(texto, clave)
print("Texto original:", texto)
print("Texto cifrado:", cifrado)
