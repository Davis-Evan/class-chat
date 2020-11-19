from socket import*

#test comment 1

clientName = "client1"
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = ""

while(message != "EXIT"):
    message = input("Input a message:")
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    incomingMessage, serverAddress = clientSocket.recvfrom(2048)
    print (incomingMessage.decode())

clientSocket.close()
