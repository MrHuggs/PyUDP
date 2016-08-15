"""Example implementation of joystick control for gopigo."""

from UDPController import UDPController
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
            left_speed = 255*max(abs(move_value), rotate_value)
            right_speed = 255*abs(move_value) + rotate_value
            if(right_speed > 255):
                left_speed -= (right_speed - 255)
                right_speed -= (right_speed - 255)
        gopigo.set_left_speed(left_speed)
        gopigo.set_right_speed(right_speed)
        if (move_value > 0):
            gopigo.fwd()
        else:
            gopigo.bwd()
