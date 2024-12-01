import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    client_socket.send("Welcome to the chat server!\n".encode())
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Message from {client_address}: {message}")
            broadcast(message, client_socket)
        except:
            break
    print(f"Closing connection from {client_address}")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                continue
server_ip = "127.0.0.1"
server_port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)
print(f"Server started on {server_ip}:{server_port}")
clients = []
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
