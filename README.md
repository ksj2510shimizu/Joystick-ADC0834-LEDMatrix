# Joystick-ADC0834-LEDMatrix

Raspberry Piで動作する、ジョイスティックの入力をMAX7219 LEDマトリクスに表示するプログラム

## 必要環境

- raspberry Pi 4
- Python3.12
- ADC0834
- MAX7219 LEDMatrix

(raspberry Pi 3や5でも多分動作するとは思います)

## 配線

[配線について](Docs/wiring.md)を参照してください

## 依存関係

### 利用ライブラリ

- gpiozero
- lgpio
- luma-led-matrix
- spidev
- [ADC0834.py](https://github.com/sunfounder/raphael-kit/blob/f19948d2714b726d37edee43bb60cb67d3a3aac2/python-pi5/ADC0834.py)

ADC0834の読み取りにSunFounder Raphael Kitの [ADC0834.py](https://github.com/sunfounder/raphael-kit/blob/f19948d2714b726d37edee43bb60cb67d3a3aac2/python-pi5/ADC0834.py) を使用しています

## 利用方法

### uvを使用する場合(推奨)

```bash
git clone https://github.com/ksj2510shimizu/Joystick-ADC0834-LEDMatrix.git
cd Joystick-ADC0834-LEDMatrix

# raphael-kitのADC0834.pyを使用するため、事前に取得する必要がある
curl -O https://raw.githubusercontent.com/sunfounder/raphael-kit/f19948d2714b726d37edee43bb60cb67d3a3aac2/python-pi5/ADC0834.py

uv sync
```

`uv sync` により自動的に必要なパッケージと仮想環境が構築されます

<details>
<summary>uvを使用しない場合</summary>

```bash
git clone https://github.com/ksj2510shimizu/Joystick-ADC0834-LEDMatrix.git
cd Joystick-ADC0834-LEDMatrix

# raphael-kitのADC0834.pyを使用するため、事前に取得する必要がある
curl -O https://raw.githubusercontent.com/sunfounder/raphael-kit/f19948d2714b726d37edee43bb60cb67d3a3aac2/python-pi5/ADC0834.py

# Python3.12を推奨
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

**今後登場する`uv run`を`.venv/bin/python`に読み替えてください**
</details>

### 実行

```bash
uv run main.py
```

## 参考

- [1.1.6 LEDドットマトリックス](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_1.1.6_led_dot_matrix_python.html)
- [2.1.9 ジョイスティック](https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python_pi5/pi5_2.1.9_joystick_python.html)
- [Markdown記法 チートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)
- ChatGPT