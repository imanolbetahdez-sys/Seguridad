import rsa
import hashlib
from cryptography.hazmat.primitives import serialization

def llavePublica():
    with open("publicKey1.pem", "rb") as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
        return publicKey
    
def llavePrivada():
    with open("privateKey1.pem", "rb") as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
        return privateKey

#obteniendo hash de documento
def hashDocumento(documentoPath):
    sha = hashlib.sha256()
    with open(documentoPath, "rb") as file:
        for blokes in iter(lambda: file.read(2048),b""):
            sha.update(blokes)
        return sha.digest()

def firmarDocumento(documentoPath, llavePublica):
    hashDoc = hashDocumento(documentoPath)
    firma = rsa.encrypt(hashDoc, llavePublica)
    with open("firmaDocumento.bin", "wb") as file:
        file.write(firma)
    print("documento firmado.")

def verificarFirma(documentoPath,llavePrivada):
    hashDoc = hashDocumento(documentoPath)
    try: 
        with open("firmaDocumento.bin", "rb") as file:
            firmaDocumento = file.read()
            hashFirmaVerificada = rsa.decrypt(firmaDocumento, llavePrivada)
            if hashDoc == hashFirmaVerificada:
                print("La firma es valida no se a alterado el documento.")
            else:
                print("La firma no es valida se a alterado el documento.")
    except Exception as e:
        print(f"Error al verificar la firma: {e}")

if __name__ == "__main__":
   documentoPath = "archivo.pdf"
   llavePrivada = llavePrivada()
   llavePublica = llavePublica()
   while True:
        print("Menu de operaciones")
        print("1.- Firmar documento")
        print("2.- Verificar firma")
        print("3.- Salir")
        operacion = input("Elige una operacion a realizar entre 1 y 2: ")
        if operacion == "1":
            firmarDocumento(documentoPath, llavePublica)
        elif operacion == "2":
            verificarFirma(documentoPath, llavePrivada)
        elif operacion == "3":
            print("Gracias por usar nuestro servicio.")
            break
        else:
            print("Elige una opcion entre 1 y 3")