import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


#try:
while True :
    # Send data
    # Look for the response
    data = sock.recv(256)
    print >>sys.stderr, 'received : %s' % data
    message = raw_input("say : ")
    #print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
#finally:
    #print >>sys.stderr, 'closing socket'
    #sock.close()
