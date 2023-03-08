import socket #Used to do stuff related to networking
import sys
import time
##end of imports ###

## initialization ##

s = socket.socket()
host = socket.gethostname()   ##gets local host name of my device
print("server will start on host:", host)  ##The host for the whole connection

#set a port
port = 8080
print(port)
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
s.listen(1) #Working with one client
conn, addr = s.accept() #connection assigned to the socket while addr is the IP addr of the client that is connecting
print(conn)
print("")
print(addr, "Has connected to the server and is now online ...")
print("")

##WORK ON ACTUAL CONNECTIONS ##
## Now we are sending Packets across ##

while 1:
    message = input(str("Input your message here >> "))
    #Have to change the message into bits bc the interface of sockets only supports bits
    if message == "End" or "end":
        break
    message = message.encode() #Changing message into bits
    conn.send(message)
    print("message has been sent....")
    print("")
    incoming_message = conn.recv(1024)  # means receive in socket in bits
    incoming_message = incoming_message.decode()  # decode the previously encoded message
    print(" Client : ", incoming_message)
    print("")