# Read Me

My partner hates when I leave a timer running after I've finished using it. This is a simple timer for use when making espresso. It counts up and changes color when in the espresso range and then it turns itself off after a minute. 

It runs on a Raspberry Pi Pico and the [Waveshare LCD 1.44](https://www.waveshare.com/wiki/Pico-LCD-1.44) inch LCD Display Module with 65K RGB Colors, 128 × 128 Pixels, SPI Interface.

The key documents in this repo are:

- [main.py](./main.py) - This script is for a coffee timer project using a Raspberry Pi Pico and a 1.44 inch LCD display. It contains functions for drawing characters and strings on the LCD framebuffer, as well as a stopwatch class. The main function initializes the display, shows a splash screen, and switches between stopwatch and sleep modes based on button presses.
- [PicoLcd144.py](./PicoLcd144.py) - Contains the driver for the LCD along with a few additions beyond the original.
- [customFont.py](./customFont.py) - This module defines the byte data for the characters '0' to '9' and ':' in a 17x24 monochrome format. It also provides functions to convert the monochrome data to RGB565 format and to create a FrameBuffer bitmap from the byte data.

To use, copy these files your Pico.

## Setting up

This is a quick setup guide. If needed, these more detailed instructions can help [Getting started with Raspberry Pi Pico](https://learn.pimoroni.com/article/getting-started-with-pico).

### Download MicroPython

The Pico base requires the [MicroPython](https://micropython.org/) firmware. The MicroPython firmware can be downloaded from [https://micropython.org/download/rp2-pico/](https://micropython.org/download/rp2-pico/).

Alternatively, you can install the Pimoroni version from here: [https://github.com/pimoroni/pimoroni-pico/releases](https://github.com/pimoroni/pimoroni-pico/releases) and contains additional libraries for Pimoroni boards. We don't use those libraries in this project but I thought I'd include it. 

Make sure to download the correct firmware for you board, including if it is a wifi-enabled vs regular board.

At the time of writing, the most recent firmware files would be:
- `pimoroni-pico-v1.21.0-micropython.uf2`
- `pimoroni-picow-v1.21.0-micropython.uf2`

### Install MicroPython onto the Pico 

To install the firmware, hold down the BOOTSEL switch on your Pico while you plug it into your computer. The device should appear in your file system. Copy the uf2 firmware file to the root of the device. When complete, the device will reboot and you can connect to it via an IDE.  

### (Optional) Install Thonny

[Thonny](https://thonny.org/) is an IDE for Python. Thonny can be used to write, edit, and run Python programs on a Raspberry Pi Pico. I swap back and forth between VS Code and Thonny as the latter sometimes works better for managing packages, resetting the device, etc.

<!-- ## Install the Pico Explorer Base Library

The Pico Explorer Base requires the Pico Explorer Base Library

This code block installs the micropython-<port>-stubs and micropython-rp2-stubs packages using pip. These packages provide stubs for the MicroPython language and the RP2 microcontroller, respectively.

```bash
pip install -I micropython-<port>-stubs
pip install -I micropython-rp2-stubs
``` -->
