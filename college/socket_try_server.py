import socket

host = "127.0.0.1"
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen()
print(f"Server is listening on {host}:{port}")
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

client_socket.send(("Hello").encode())

data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

client_socket.close()
server_socket.close()
