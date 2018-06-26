#!/usr/bin/python

import  socket 
#            type of ip v4 ,      type of protocol UDP  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=raw_input("enter your command : ")
s.sendto(msg,("192.168.43.68",8000))




