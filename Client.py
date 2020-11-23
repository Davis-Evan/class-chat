import socket
import threading

user = input("Username: ")

HOST = "127.0.0.1"
PORT = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(False)


def rec():
    while True:
        try:
            mess = s.recv(2048).decode()
            if mess == "Username":
                s.send(user.encode())
            else:
                print(mess)
        except Exception:
            continue


def write():
    while True:
        message = f'{user} : {input("")}'
        s.send(message.encode())


rec = threading.Thread(target=rec)
rec.start()

write = threading.Thread(target=write)
write.start()
