from socket import *

# This Server communicates with one client


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("server is ready")

serverRunning = False
outgoingMessage = ""
incomingMessage = ""
outgoingAddress = ('127.0.0.1', 0)


def main():
    maintainConnection()


def initConnection():
    message, incomingAddress = serverSocket.recvfrom(2048)
    outgoingMessage = "Connected to Server"
    outgoingAddress = incomingAddress
    serverSocket.sendto(outgoingMessage.encode(), outgoingAddress)
    return True


def maintainConnection():
    serverRunning = initConnection()
    while serverRunning:
        message, incomingAddress = serverSocket.recvfrom(2048)
        message = message.decode()
        outgoingMessage = "Your message was received, it was: " + message
        outgoingAddress = incomingAddress
        serverSocket.sendto(outgoingMessage.encode(), outgoingAddress)

        if (incomingMessage == "EXIT"):
            serverRunning = False
            print("Server Killed")


main()
