#!/usr/bin/python
# -*- coding: utf-8 -*-
print("-Start client.py")
import socket

sock = socket.socket()

if raw_input("Do you want to connect automatically?\nEnter 't' or 'n' ") == "t":
    host = 'localhost'
    port = 9090
elif "n":
    host = raw_input("enter hostname\n")
    port = int(raw_input("enter port number\n"))
else:
    print("you should have entered 't' or 'n' ")

sock.connect((host, port))
print("-server connection established")

s = "0"
while s != "exit":
    s = raw_input("please write your message\n")
    sock.send(s)
    print("-sending data to server")

    print("-dreceiving data from the server")
    data = sock.recv(1024)
    print("data: " + data)

print("-disconnecting from the server")
sock.close()