import socket
import ssl

HOST = '192.168.10.1'   # IP del servidor
PORT = 4001             # Puerto del servidor

contexto = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
contexto.load_verify_locations(cafile="certificado.pem") 

try:
    with socket.create_connection((HOST, PORT)) as conexion:
        with contexto.wrap_socket(conexion, server_hostname="192.168.10.1") as cliente:
            print("Conexión realizada con servidor TLS usando certificado propio")
            mensaje = input("Escribe el mensaje que quieres enviar al servidor TLS: ")
            cliente.sendall((mensaje + "\n").encode("utf-8"))
            print("Mensaje enviado al servidor TLS")

except Exception as e:
    print("Error al conectar con el servidor TLS:", e)