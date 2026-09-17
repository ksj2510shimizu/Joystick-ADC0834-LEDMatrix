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
        
        print(f"X座標: {x_position} Y座標: {y_position}")
        if (joystick.is_sw_pressed()):
            print("スイッチが押さています")

        led_matrix.draw(x_position, y_position)
        sleep(0.01)
    except KeyboardInterrupt:
        pass