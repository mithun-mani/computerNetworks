#! /usr/bin/env python3
# Echo Server
#Mithun Manivannan, mm2356, CS 356-007
import sys
import socket
import struct
import time
import random
# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
f = open("dns-master.txt", "r")
arr =[]
word = ""
for x in f:
    word+=x
f.close()
word = word.replace(" ","")
spl = word.split("domain")
newStr = spl[1]
newStr = newStr.replace("AIN"," ")
newStr = newStr.replace("\n"," ")
arr = newStr.split(" ")
arr.pop(0)
dict = {}
for i in range(0,(len(arr)-1), 2):
    val = arr[i+1]
    newVal = val[:4] + ' ' + val[4:]
    dict[arr[i]] = newVal
# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    #realData = struct.unpack("!hhihh10s",data)
    recvData = struct.unpack('!hhihh', data[0:12])
    realData = struct.unpack('!hhihh' + str(recvData[3] - 5) + 's', data)
    value = ""
    vlength = 0
    returnCode = 0
    key = realData[5].decode()
    if key in dict:
        value = dict[key]
        vlength = len(value)
    else:
        returnCode = 1
    # Echo back to client
    newData = struct.pack("!hhihh" + str(len(value)) + 's',2, returnCode,realData[2], realData[3], vlength, value.encode())
    serverSocket.sendto(newData,address)
