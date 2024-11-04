# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:42:51 2024

@author: Reza Farzam 20137189
"""
#importing the library
import socket

#create a varble for socket
c = socket.socket()

#specify the server name and its port
c.connect(("localhost",1234))

# send user name to the server
username = input("Enter your name: ")
c.send(bytes(username,"utf-8"))

# recieve massege from server
print(c.recv(1024).decode())

#terminate the connection
c.close()
