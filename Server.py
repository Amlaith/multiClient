import socket
import os
from _thread import *

server_socket = socket.socket()
host = '127.0.0.1'
port = 1233
thread_count = 0

try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a connection..')
server_socket.listen(5)

def threaded_client(connection, address):
    global thread_count
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

    thread_count -= 1
    print('Thread Number: ' + str(thread_count))
    exit()


while True:
    client, address = server_socket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (client, address))
    thread_count += 1
    print('Thread Number: ' + str(thread_count))

server_socket.close()
