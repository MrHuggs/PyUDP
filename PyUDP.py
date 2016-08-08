from socket import *
import time

UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket(AF_INET, # Internet
                     SOCK_DGRAM) # UDP

sock.bind(('', 0))

# On my main machine, the physical NIC is actually the second adpate for some reason.
# We need to bind to that address or the broadcasts go out the first NIC, which is some 
# sort of virtual adapter.
# sock.bind(('192.168.1.105', 0))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

num = 0

while 1:
    sent = sock.sendto(MESSAGE, ('<broadcast>', UDP_PORT))
    print "Sending...{0} - {1} bytes sent.".format(num, sent)
    num += 1
    time.sleep(2)