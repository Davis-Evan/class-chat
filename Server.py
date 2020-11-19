from socket import*

# This Server communicates between TWO clients
# test comment 3

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("server is ready")

serverRunning = True
addresses = []
inAddInd = 0
outAddInd = 0
outgoingMessage = ""
incomingMessage = ""
outgoingAddress = ('127.0.0.1', 0)



while serverRunning:
    #connect to server
    message, incomingAddress = serverSocket.recvfrom(2048)
    if (incomingAddress in addresses):
        print("Address exists")
    else:
        addresses.append(incomingAddress)
        print("Address appended")
        outgoingMessage = "Connected to Server"
        serverSocket.sendto(outgoingMessage.encode(), incomingAddress)

    ###############

    #can use index here
    if (len(addresses) >= 2):
        if (incomingAddress == addresses[0]):
            outgoingAddress = addresses[1]
        else:
            outgoingAddress = addresses[0]

        incomingMessage = message.decode()
        outgoingMessage = incomingMessage
        serverSocket.sendto(outgoingMessage.encode(), outgoingAddress)



    if (incomingMessage == "EXIT" ):
        serverRunning = False
        print("Server Killed")
