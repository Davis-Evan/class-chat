import socket
import threading

HOST = "127.0.0.1"
PORT = 12000

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.bind((HOST, PORT))
#    s.listen()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

user_ids = {}
clients = []


def main():
    print("Main")
    receive()


def broadcast(mess):
    mess = mess.encode()
    for cs in clients:
        cs.send(mess)


def in_sys_check(addr):
    mess = "User not registered"
    addr.send(mess.encode())


def handle(csock, addr, user_id):
    mess = csock.recv(2048)
    broadcast(mess)


def receive():
    while True:
        csock, addr = s.accept()
        csock.send("RequestUserID".encode())
        user_id = csock.recv(2048).decode()
        user_ids[user_id] = addr
        clients.append(csock)
        #broadcast((user_id + " just joined.").encode())
        broadcast("Someone's here.")
        t = threading.Thread(target=handle, args=(csock, addr, user_id))
        t.start()


main()

