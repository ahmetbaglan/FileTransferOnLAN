#!/usr/bin/env python

from socket import *


host=""
port = 13001

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((host,port))

addr = (host,port)
buf=1024

f = open("got.xlsx",'wb')
print("listening")
data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("File Downloaded")
