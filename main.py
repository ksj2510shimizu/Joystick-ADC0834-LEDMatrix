from joystick import Joystick, MovingAvg
from led_matrix import LEDMatrix
from time import sleep

joystick = Joystick()
led_matrix = LEDMatrix()

x_avg = MovingAvg(10)
y_avg = MovingAvg(10)

while (True):
    try:
        x_position = x_avg.add_val(joystick.get_x_ratio()) * 7
        y_position = y_avg.add_val(joystick.get_y_ratio()) * 7

        led_matrix.draw(x_position, y_position)
        sleep(0.01)
    except KeyboardInterrupt:
        pass