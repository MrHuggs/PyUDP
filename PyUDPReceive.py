import socket
import select
import struct

UDP_PORT = 5005
timeout = 1

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))

sock.setblocking(0)

num = 0

while True:

    ready = select.select([sock], [], [], timeout)
    if ready[0]:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        num += 1
        print num
        try:
            joy_data = struct.unpack("ff", data)
        except:
            joy_data = "Data error"

        print "received message {0}:".format(num), joy_data
    else:
        print "No data received in {0} seconds.".format(timeout)

