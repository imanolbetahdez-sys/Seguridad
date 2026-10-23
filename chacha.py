import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

keyChacha = os.urandom(32)
nonceChacha = os.urandom(16)
data = "Mensaje a encriptar"
data2 = data.encode("UTF-8")


ChiperChacha = Cipher(algorithms.ChaCha20(keyChacha, nonceChacha), None)
encriptadorChacha = ChiperChacha.encryptor()
cifradoChacha = encriptadorChacha.update(data) + encriptadorChacha.finalize()

desencriptadorChacha = ChiperChacha.decryptor
descifradoChacha = desencriptadorChacha.update(cifradoChacha) + desencriptadorChacha.finalize()

print("llave")
print(keyChacha)
print("cifrado")
print(cifradoChacha)
print("Descifrado")
print(descifradoChacha.decode("UTF-8"))
