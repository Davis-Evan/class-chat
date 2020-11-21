import socket

host = '127.0.0.1'
port = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    connected = True
    while connected:
        with conn:
            print('Connected by', addr)
            while True:
                message = "Received from client: " + (conn.recv(1024)).decode()
                conn.sendall(message.encode())
