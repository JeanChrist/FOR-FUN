# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:30:24 2017

@author: C
"""


from socket import *

HOST = '::1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET6, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print (data.decode('utf-8'))
    
tcpCliSock.close()
