# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:38:49 2024

@author: Reza Farzam 20137189
"""

# Import the socket library
import socket

#create varuble for socket
s = socket.socket()

print("Socket created")

#specify the server name and port
s.bind(("localhost",1234))

# open the ports for connection
s.listen(3)
print("Waiting for connections")

#accept the clients request
c, addr, = s.accept()
c.send(bytes("WLC to reza server","utf-8"))      

#recieve the client massege
name = c.recv(1024).decode()
print("connected with ",addr,name) 

#terminate the program    
c.close() 
s.close()
    
