# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:38:49 2024

@author: rezaf
"""

import socket

s = socket.socket()

print("Socket created")

s.bind(("localhost",1234))

s.listen(3)
print("Waiting for connections")

c, addr, = s.accept()
c.send(bytes("WLC to reza server","utf-8"))      

name = c.recv(1024).decode()
print("connected with ",addr,name) 

    
c.close() 
s.close()
    