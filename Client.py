import socket

client_socket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    client_socket.connect((host, port))
except socket.error as e:
    print(str(e))
else:
    print(client_socket.recv(1024).decode('utf-8'))
    while True:
        message = input('Say Something: ')
        client_socket.send(str.encode(message or 'dummy ping'))
        response = client_socket.recv(1024).decode('utf-8')
        if response == 'exit':
            print('Connection closed')
            break
        print(response)
