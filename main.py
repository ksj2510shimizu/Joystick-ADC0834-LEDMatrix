from joystick import Joystick
from led_matrix import LED_Matrix
from time import sleep

joystick = Joystick()
led_matrix = LED_Matrix()

while (True):
    x_position = joystick.get_x_ratio() * 7
    y_position = joystick.get_y_ratio() * 7
    
    led_matrix.draw(x_position, y_position)
    sleep(0.1)
