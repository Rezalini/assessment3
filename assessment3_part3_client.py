# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:42:51 2024

@author: rezaf
"""

import socket

c = socket.socket()

c.connect(("localhost",1234))

username = input("Enter your name: ")
c.send(bytes(username,"utf-8"))


print(c.recv(1024).decode())

c.close()
