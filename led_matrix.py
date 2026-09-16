from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

class LED_Matrix:
    def __init__(self):
        self._serial = spi(port=0, device=0, gpio=noop())
        self._device = max7219(self._serial, rotate=3)

    def draw(self, x_position: float, y_position: float):
        with canvas(self._device) as draw:
            draw.rectangle(
                (
                    int(x_position),
                    int(y_position),
                    int(x_position) + 1,
                    int(y_position) + 1
                ),
                fill="white"
            )