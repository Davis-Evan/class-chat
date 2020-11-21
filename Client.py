import socket, threading

HOST = "127.0.0.1"
PORT = 12000

userID = input("Input a username: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(False)


def main():
    rec = threading.Thread(target=receive)
    rec.start()
    wr = threading.Thread(target=write)
    wr.start()


def write():
    while True:
        mess = f'{userID} : {input(">> ")}'
        s.send(mess.encode())

def receive():
    while True:
        try:
            mess = s.recv(2048).decode()
            if mess == "RequestUserID":
                s.send(userID.encode())
            else:
                print(mess)
        except Exception:
            print(Exception)


main()