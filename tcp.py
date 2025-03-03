import socket

def handle_client(client_socket):
    client_socket.sendall(b"Open")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode())

    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)

while True:
    client_socket, addr = server.accept()
    handle_client(client_socket)
