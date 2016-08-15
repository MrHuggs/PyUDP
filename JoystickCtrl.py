"""Example implementation of joystick control for gopigo."""

from PyUDPReceive import UDPController
import gopigo

controller = UDPController()

while(True):
    left_speed = 0
    right_speed = 0
    if controller.read():
        move_value = controller.y
        rotate_value = controller.x
        if rotate_value > 0:
            left_speed = 255*(abs(move_value) + rotate_value)
            right_speed = 255*max(abs(move_value), rotate_value)
            if(left_speed > 255):
                right_speed -= (left_speed - 255)
                left_speed -= (left_speed - 255)
        else:
            left_speed = 255*max(abs(move_value), abs(rotate_value))
            right_speed = 255*(abs(move_value) + rotate_value)
            if(right_speed > 255):
                left_speed -= (right_speed - 255)
                right_speed -= (right_speed - 255)

        if left_speed != 0 or right_speed != 0:
            print "controls: ({0}, {1})".format(controller.x, controller.y)
            dir = "forward" if move_value >= 0  else "back"
            print "{0} left:{1} right:{2}".format(dir, left_speed, right_speed)

        gopigo.set_left_speed(int(left_speed))
        gopigo.set_right_speed(int(right_speed))
        if (move_value > 0):
            gopigo.fwd()
        else:
            gopigo.bwd()
