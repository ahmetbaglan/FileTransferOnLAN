__author__ = 'ahmet'

from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
host = "192.168.1.57"
port = 13001
buf = 1024
addr = (host,port)

f=open("a.xlsx", "rb")
data = f.read(buf)

s.sendto(data, addr)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()
