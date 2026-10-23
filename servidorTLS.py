import socket
import ssl
HOST = '192.168.10.1'
PORT = 4001

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain('certificado.pem','private.pem')

with socket.socket() as servidor:
    
    servidor.bind((HOST, PORT))
    servidor.listen()
    print("Esperando conexion segura del cliente TLS")

    conexion, _= servidor.accept()

    with conexion: 
        with contexto.wrap_socket(conexion,server_side=True) as cliente:
            print('conexion segura',cliente.version())

            with cliente:
                datos = cliente.recv(1024).decode('utf-8').strip()
                print("Mensaje recibido del cliente:", datos)
