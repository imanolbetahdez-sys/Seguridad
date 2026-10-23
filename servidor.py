import socket

HOST='192.168.10.1'
PUERTO= 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PUERTO))
        servidor.listen()
        print(f"Servidor escuchando en {HOST}:{PUERTO}")
        conexion, direccion = servidor.accept()
        with conexion:
            conexion.settimeout(10)
            print(f"Conexion establecida desde {direccion}")
            with conexion.makefile('rb') as ingreso:
                linea = ingreso.readline().decode('utf-8').strip
                print(f"Recibido: {linea}")

if __name__=="__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: ")