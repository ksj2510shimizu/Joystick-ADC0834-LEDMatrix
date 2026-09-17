# 配線について

Raspberry Pi と Raphael Kit の GPIO Extension Board と Breadboard が接続されている前提です

## 必要なもの

- MAX7219 LED Matrix ×1
- Joystick ×1
- ADC0834 ×1
- ジャンパーワイヤー たくさん
- 10kΩ抵抗 ×1

## 配線先

[1.1.6 LEDドットマトリックス](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_1.1.6_led_dot_matrix_python.html) と [2.1.9 ジョイスティック](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_2.1.9_joystick_python.html) と同じ配線です

### MAX7219 LED Matrix

MAX7219 LED Matrix → Raspberry Pi

| LED Matrix Module | T-Board Name |
| :----: | :----: |
| VCC | 5v0 |
| GND | GND |
| DIN | SPIMOSI |
| CE0 | SPICE0 |
| CLK | SPISCLK |

参考: [1.1.6 LEDドットマトリックス](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_1.1.6_led_dot_matrix_python.html)

### Joystick

ADC0834 → Raspberry Pi

| ADC0834 | T-Board Name |
| :----: | :----: |
| V+ | 5v0 |
| CS | GPIO17 |
| CH0 | - |
| CH1 | - |
| CH2 | - |
| CH3 | - |
| DGTL GND | GND |
| VCC | 5v0 |
| DI | GPIO27 |
| CLK | GPIO18 |
| SARS | - |
| DO | GPIO27 |
| REF | 5v0 |
| ANLG GND | GND |

Joystick → ADC0834 / Raspberry Pi

| Joystick | ADC0834 | T-Board Name |
| :----: | :----: | :----: |
| GND | - | GND |
| +5V | - | 5v0 |
| VRx | CH0 | - |
| VRy | CH1 | - |
| SW | - | 10kΩ → GPIO22 |

**必ずSWから10kΩを抵抗を経由してGPIO22に接続するようにしてください**

参考: [2.1.9 ジョイスティック](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_2.1.9_joystick_python.html)