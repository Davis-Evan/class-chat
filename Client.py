import socket
import threading

user = input("Username: ")
HOST = "127.0.0.1"
PORT = 8000

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
        mess = f'{user} : {input("")}'
        s.send(mess.encode())


def main():
    rec_run = threading.Thread(target=rec)
    rec_run.start()
    write_run = threading.Thread(target=write)
    write_run.start()


main()
