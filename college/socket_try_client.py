import socket

host = "127.0.0.1"
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")
welcome_msg = client_socket.recv(1024).decode()
print(f"Server says: {welcome_msg}")
client_socket.send(("Its me Hi").encode())

client_socket.close()
