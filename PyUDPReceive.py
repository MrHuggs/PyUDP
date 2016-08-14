import socket
import select
import struct
import time



class UDPController:

    # Listens on a UDP port for gamepad data, and provides the most recently recieved data.
    def __init__(self, port = 5005):
        self.updPort = port
        self.reset()

        self.sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        self.sock.bind(('', self.updPort))

        self.sock.setblocking(0)
    
    def reset(self):
        self.y = 0
        self.x = 0
        self.num = 0
        self.lastPacket = time.time()
         
    def _checkTimeout(self):
        dt = time.time() - self.lastPacket
        if dt > 2:
            self.reset()
            return True
        return False

    def _parsePacket(self, data):
        self.num += 1
        try:
            joy_data = struct.unpack("ff", data)
            self.x = joy_data[0]
            self.y = joy_data[1]
            self.lastPacket = time.time()
        except:
            print "Data error encountered."

    def read(self):
        ready = select.select([self.sock], [], [], 0)

        if not ready[0]:
            return self._checkTimeout()

        data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes

        self._parsePacket(data)
        return True

    
# -------------------------------------------------------------------------------
# Simple test for running from the command line
#
if __name__ == '__main__':

    controller = UDPController()

    while True:
        if controller.read():
            print "Controller packet {0} - ({1}, {2})".format( controller.num, controller.x, controller.y)


