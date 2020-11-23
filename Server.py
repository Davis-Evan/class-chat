import threading
import socket

HOST = "127.0.0.1"
PORT = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

clients = []
usernames = {}


def fwd_all(mess):
    mess = mess.encode()
    for cs in clients:
        cs.send(mess)


def private_mess(raddr, mess, ssock):
    pMess = "Private Message: "
    mess = (pMess + mess).encode()

    if raddr not in usernames:
        mess = "User not in system"
        mess = mess.encode()
        ssock.send(mess)
    else:
        for c in clients:
            peer = c.getpeername()
            if(peer[1] == usernames[raddr][1]):
                c.send(mess)


def handle(csock, caddr, username):
    while True:
        mess = (csock.recv(2048)).decode()
        fwd_all(mess)


def receive():
    prompt = "Username"
    prompt = prompt.encode()
    while True:
        csock, caddr = s.accept()
        csock.send(prompt)
        username = csock.recv(2048).decode()
        usernames[username] = caddr
        clients.append(csock)
        mess = username + " has joined the group."
        fwd_all(mess)
        thread = threading.Thread(target = handle, args = (csock, caddr, username))
        thread.start()

print("Server running")
receive()