import socket 
host = '192.168.10.2'
puerto = 5000

def main():
    mensaje = input("Ingresa el mensaje para el servidor: ")
    with socket.create_connection((host, puerto), timeout=10 ) as cliente:
        cliente.sendall((mensaje +'\n').encode('utf-8'))
        print(f"mensaje enviado al servidor: {mensaje}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERRO: {e}")