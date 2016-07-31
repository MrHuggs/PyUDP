import socket

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))

num = 0

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    num += 1
    print num
    print "received message:", data