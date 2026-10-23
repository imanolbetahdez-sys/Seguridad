"""
Cliente TLS.

Uso:
    python cliente_tls.py                  -> se conecta a 192.168.10.1:4001
    python cliente_tls.py 192.168.10.1     -> IP del servidor
"""
import socket
import ssl
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else '192.168.10.1'  # debe estar en el SAN del certificado
PORT = 4001

# Verifica el certificado y el nombre/IP del servidor (no desactivar)
contexto = ssl.create_default_context(
    ssl.Purpose.SERVER_AUTH,
    cafile='certificado.crt'
)
contexto.minimum_version = ssl.TLSVersion.TLSv1_2

try:
    with socket.create_connection((HOST, PORT), timeout=10) as conexion:
        with contexto.wrap_socket(conexion, server_hostname=HOST) as cliente:
            print('Conexion realizada con servidor TLS:', cliente.version())
            mensaje = 'conexión segura.......\n'  # el \n permite que readline() del servidor termine
            cliente.sendall(mensaje.encode('utf-8'))
            print('Mensaje enviado al servidor TLS')

            with cliente.makefile('rb') as ingreso:
                respuesta = ingreso.readline().decode('utf-8').strip()
            print('Respuesta del servidor:', respuesta)

except ssl.SSLCertVerificationError as e:
    print('El certificado no es valido para este servidor:', e)
except (ConnectionError, TimeoutError, socket.gaierror) as e:
    print('No se pudo conectar con el servidor:', e)
except ssl.SSLError as e:
    print('Error TLS:', e)
