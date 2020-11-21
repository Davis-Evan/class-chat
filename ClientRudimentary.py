import socket

Host = '127.0.0.1'
Port = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    connected = True
    while connected:
        messOut = input("Input a message: ")
        s.sendall(messOut.encode())
        messIn = s.recv(1024)
        print(messIn.decode())
