#!/usr/bin/env python

from socket import *
import sys
import select

host=""
port = 13010

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((host,port))

addr = (host,port)
buf=1024

f = open("got.xlsx",'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        s.sendto(bytes("hello",'utf-8'),("192.168.1.60",13010))
        print ("going on")
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("File Downloaded")
