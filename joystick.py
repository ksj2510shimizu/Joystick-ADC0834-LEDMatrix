from gpiozero import Button
import ADC0834

# SWの接続先
sw_pin = 22

class Joystick:
    def __init__(self):
        self._sw = Button(sw_pin)
        ADC0834.setup()
    
    def get_x_val(self) -> int:
        return ADC0834.getResult(0)

    def get_y_val(self) -> int | None:
        return ADC0834.getResult(1)

    def is_sw_pressed(self) -> bool:
        return self._sw.is_pressed