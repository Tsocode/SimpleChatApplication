import socket #Used to do stuff related to networking
import sys
import time


s = socket.socket()
host = input(str("Enter the host name of the server: "))
port = 8080
s.connect((host,port))
print("Connected to chat server")
while 1:
    incoming_message = s.recv(1024)#means receive in socket in bits
    incoming_message = incoming_message.decode()#decode the previously encoded message
    print(" Server : ", incoming_message)
    print("")
    message = input(str("Input your message here >> "))
    if message == "End" or "end":
        break
    # Have to change the message into bits bc the interface of sockets only supports bits
    message = message.encode()  # Changing message into bits
    s.send(message)
    print("message has been sent....")
    print("")