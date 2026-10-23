import socket
import ssl

HOST = '192.168.10.1'   # IP del servidor
PORT = 4001             # Puerto del servidor

# Crear contexto TLS usando tu certificado propio
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain(certfile="certificado.pem", keyfile="private.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen(5)  # permitir hasta 5 conexiones en espera
    print("✅ Servidor TLS escuchando en", HOST, "puerto", PORT)

    while True:
        conexion, addr = servidor.accept()
        print("📡 Cliente conectado desde:", addr)
        with conexion:
            try:
                with contexto.wrap_socket(conexion, server_side=True) as cliente:
                    print("🔒 Conexión segura establecida con versión:", cliente.version())

                    # Recibir mensaje del cliente
                    with cliente.makefile('rb') as entrada:
                        mensaje = entrada.readline().decode('utf-8').removesuffix('\n')
                    print("📩 Mensaje recibido del cliente:", mensaje)

            except Exception as e:
                print("❌ Error en la conexión TLS:", e)