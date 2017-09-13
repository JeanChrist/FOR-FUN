# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:24:25 2017

@author: C
"""

from time import ctime 
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    print ('[%s] (jc): %s' % (ctime(),data))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print (data.decode('utf-8'))
    
tcpCliSock.close()
