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

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    rand = random.randint(0,10)
    data, address = serverSocket.recvfrom(1024)
    realData = struct.unpack("!HH",data)
    
    if rand < 4:
        print("Message with sequence number " + str(realData[1]) + " dropped")
        continue;
    # Echo back to client
    print("Responding to ping request with sequence number " + str(realData[1]))
    newData = struct.pack("!HH",2,realData[1])
    serverSocket.sendto(newData,address)
