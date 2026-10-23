import hashlib

texto = "prueba de hash"
hashFijo = hashlib.sha1(texto.encode("UTF-8")).hexdigest()
print("Tetxo original: ", texto)
print("Hash has1: ", hashFijo )

hashFijo2 = hashlib.sha256(texto.encode("UTF-8")).hexdigest()
print("Hash sha 256: ", hashFijo2)

with open("copo.png", "rb") as file:
    copo = file.read()
    hashCopo = hashlib.sha256(copo).hexdigest()
    file.close()
print("Hash sha256 de copo: ", hashCopo)