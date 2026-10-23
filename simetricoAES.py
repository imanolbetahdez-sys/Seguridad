import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

keyAES = os.urandom(32)
paddingAES = padding.ANSIX923(128).padder()
data = "Mensaje a encriptar"
data2 = data.encode("UTF-8")
cipher = Cipher(algorithms.AES(keyAES), modes.CBC(os.urandom(16)))
cifrador = cipher.encryptor()
textoCifrado = cifrador.update(paddingAES.update(data2) + paddingAES.finalize()) + cifrador.finalize()
print("Mensaje a encriptar: " + data)
print("Texto cifrado: " + textoCifrado)
descifrador = cipher.decryptor()
unpadder = padding.ANSIX923(128).unpadder()
textoDescifrado = unpadder.update(descifrador.update(textoCifrado) + descifrador.finalize) + unpadder.finalize
print("Mensaje descifrado: " + textoDescifrado.decode("UTF-8"))