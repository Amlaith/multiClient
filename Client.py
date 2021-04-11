import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
else:
    print(ClientSocket.recv(1024).decode('utf-8'))
    while True:
        Input = input('Say Something: ')
        ClientSocket.send(str.encode(Input or 'dummy ping'))
        Response = ClientSocket.recv(1024).decode('utf-8')
        if Response == 'exit':
            print('Connection closed')
            break
        print(Response)
