"""Example implementation of joystick control for gopigo."""

from PyUDPReceive import UDPController
import gopigo
from math import copysign

controller = UDPController()


def calc_speed(move_value, rotate_value):
    """Calculate motor speeds based on joystick inputs"""
    left_speed, right_speed = abs(move_value)
    left_speed += rotate_value
    right_speed -= rotate_value
    right_speed = min(max(right_speed, -1), 1)
    left_speed = min(max(left_speed, -1), 1)
    left_speed *= copysign(255, move_value)
    right_speed *= copysign(255, move_value)
    return [left_speed, right_speed]

while(True):
    left_speed = 0
    right_speed = 0
    if controller.read():
        move_value = controller.y
        rotate_value = controller.x
        [left_speed, right_speed] = calc_speed(move_value, rotate_value)
        if left_speed != 0 or right_speed != 0:
            print "controls: ({0}, {1})".format(controller.x, controller.y)
            dir = "forward" if move_value >= 0  else "back"
            print "{0} left:{1} right:{2}".format(dir, left_speed, right_speed)
        gopigo.set_left_speed(int(abs(left_speed)))
        gopigo.set_right_speed(int(abs(right_speed)))
        if left_speed > 0:
            if right_speed > 0:
                gopigo.fwd()
            else:
                gopigo.right_rot()
        else:
            if right_speed > 0:
                gopigo.left_rot()
            else:
                gopigo.bwd()
