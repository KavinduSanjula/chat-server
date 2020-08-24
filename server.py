import socket
import threading

IP = '127.0.0.1' #Localhost
PORT = 4444
ADDRESS = (IP,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()

clients = {}

def broadcast(message):
    nicknames = clients.keys()
    for nickname in nicknames:
        clients[nickname].send(message.encode('utf-8'))


def handle_client(client_socket,nickname):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message)
        except:
            broadcast(f"{nickname} left the chat.")
            client_socket.close()
            break
        
        
print(f"Server is listning on {ADDRESS}")
while True:
    client_socket,addr = server.accept()
    client_socket.send("NICK".encode('utf-8'))
    nickname = client_socket.recv(1024)
    print(f"New client on {addr} Nickname - {nickname}")
    clients[nickname] = client_socket
    thread = threading.Thread(target=handle_client,args=(client_socket,nickname))
    thread.start()
    broadcast(f"{nickname} joind to the chat.")

    