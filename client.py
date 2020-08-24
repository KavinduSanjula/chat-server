import socket
import threading

IP = '127.0.0.1' #Localhost
PORT = 4444
ADDRESS = (IP,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(ADDRESS)

nickname = input('Enter Nickname: ')


def receve():
    while True:
        try:
            msg = server.recv(1024).decode('utf-8')
            if msg == 'NICK':
                server.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            server.close()
            break

def write():
    while True:
        msg = f"{nickname}: "+input()
        try:
            server.send(msg.encode('utf-8'))
        except:
            server.close()
            break

receve_thread = threading.Thread(target=receve)
write_thread = threading.Thread(target=write)

receve_thread.start()
write_thread.start()

