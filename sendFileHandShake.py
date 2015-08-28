__author__ = 'ahmet'

from socket import *


s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
host = "192.168.1.57"
port = 13010
buf = 1024
addr = (host,port)
s.bind(("",port))

f=open("a.xlsx", "rb")
data = f.read(buf)

while (data):
    s.sendto(data,addr)
    print("sending ...")
    data,addr = s.recvfrom(buf)
    if(data ==  "hello"):
        print ("so Sent")
    data = f.read(buf)
s.close()
f.close()
