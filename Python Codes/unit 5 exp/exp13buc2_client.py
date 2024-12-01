import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except:
            break
server_ip = "127.0.0.1"
server_port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()
while True:
    message = input()
    if message.lower() == 'exit':
        client_socket.close()
        break
    client_socket.send(message.encode())
