from socket import *
import time

UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket(AF_INET, # Internet
                     SOCK_DGRAM) # UDP

sock.bind(('', 0))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    sock.sendto(MESSAGE, ('<broadcast>', UDP_PORT))
    print "Sending..."
    time.sleep(2)