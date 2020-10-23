#Mithun Manivannan
#mm2356
#CS 356-007
#! /usr/bin/env python3
# Echo Client
import sys
import socket
import struct
import time
import random
# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
message_id = random.randint(0,100)
print("Sending request to " + str(host) + ", " + str(port) + ":  ")
print("Message ID: " + str(message_id))
newHostname = hostname
newHostname += " A IN"
qlength = len(newHostname)
print("Question Length: " + str(qlength) + " bytes")
print("Answer Length: 0 bytes")
print("Question: " + hostname + " A IN\n\n\n")
data = struct.pack('!hhihh' + str(len(hostname)) + 's',1,0, message_id, qlength, 0,hostname.encode())
# Create UDP client socket. Note the use of SOCK_DGRAM
for i in range(1,4):
    try:
        # Pinging server
        clientsocket.sendto(data,(host, port))
        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(1024)
        recvData = struct.unpack('!hhihh', dataEcho[0:12])
        dataEcho = struct.unpack('!hhihh' + str(recvData[4]) + 's', dataEcho)
        print("Received response from " + str(host) + " " + str(port) + ": ")
        print("Return Code: " + str(dataEcho[1]))
        print("Message ID: " + str(dataEcho[2]))
        print("Question Length: " + str(qlength) + " bytes")
        if (dataEcho[1] == 0):
            print("Answer Length: " + str(qlength + dataEcho[4] + 1) + " bytes")
        else:
            print("Answer Length: 0 bytes")
        print("Question: " + hostname + " A IN ")
        if (dataEcho[1] == 0):
            print("Answer: " + hostname + " A IN " + str(dataEcho[5].decode()))
        break;
    except socket.timeout:
        print("Request timed out")
        print("Sending request to " + str(host) + ", " + str(port) + ":  ")
clientsocket.close()
