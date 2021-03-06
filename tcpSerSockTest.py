# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:02:12 2017

@author: C
"""

from socket import *
from time import ctime 

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print ('[%s] (from jc): %s' % (
                ctime(),data.decode()))
        senddata = input('> ')
        print ('[%s] (server): %s' % (ctime(), senddata))
        tcpCliSock.send('[%s] (from server): %s'.encode() % (
                ctime().encode(),senddata.encode()))
        
    tcpCliSock.close()
tcpSerSock.close()