import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a connection..')
ServerSocket.listen(5)

def threaded_client(connection, address):
    global ThreadCount
    connection.send(str.encode('Welcome to the Server, ' + ':'.join(map(str, address))))
    while True:
        data = connection.recv(2048)
        data = data.decode('utf-8')
        if data == 'exit':
            connection.sendall(str.encode(('exit')))
            break
        reply = 'Server Says: ' + data
        connection.sendall(str.encode((reply)))

    print('Connection closed: ' + ':'.join(map(str, address)))
    connection.close()

    ThreadCount -= 1
    print('Thread Number: ' + str(ThreadCount))
    exit()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()
