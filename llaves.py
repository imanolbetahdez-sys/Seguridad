import rsa
publicKey, privateKey = rsa.newkeys(2048)
with open("publicKey1.pem", "wb") as f:
    f.write(publicKey.save_pkcs1(format='PEM'))
with open("privateKey1.pem", "wb") as f:
    f.write(privateKey.save_pkcs1(format='PEM'))