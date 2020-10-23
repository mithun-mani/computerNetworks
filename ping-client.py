#Mithun Manivannan
#mm2356
#CS 356-007
#! /usr/bin/env python3
# Echo Client
import sys
import socket
import struct
import time
# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
print("Pinging " + host + ", " + str(port) + ":  ")
receivedCounter = 0
transmitCount =0
rttList= []
# Create UDP client socket. Note the use of SOCK_DGRAM
for i in range(1,11):
    clientTime = time.time()
    data = struct.pack("!HH",1,i)
    try:
        # Pinging server
        clientsocket.sendto(data,(host, port))
        transmitCount += 1
        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(1024)
        serverTime = time.time()
        rtt = abs(clientTime - serverTime)
        rttList.append(rtt)
        dataEcho = struct.unpack("!HH", dataEcho)
        messageType = dataEcho[0]
        if (messageType == 2):
            receivedCounter+=1
        print("Ping message number " + str(i) + " RTT: " + str(rtt) + " secs")
    except socket.timeout:
        print("Ping message number " + str(i) + " timed out")
percentage = (float(transmitCount-receivedCounter)/transmitCount)*100
print("Statistics:\n" +str( transmitCount) +" packets transmitted, " + str(receivedCounter) +" received, " + str(percentage) + " % packet loss")
average = sum(rttList)/len(rttList)
print("Min/Max/Avg RTT: " + str(min(rttList)) + "/ " + str(max(rttList)) + "/ " + str(average))
clientsocket.close()
