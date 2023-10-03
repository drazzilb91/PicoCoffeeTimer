import picographics
import framebuf
from PicoLcd144 import LCD_1inch44

LCD = LCD_1inch44()

# This is an example of creating a framebuffer for a 128x128 pixel display
fb = framebuf.FrameBuffer(bytearray(128 * 128 * 2), 128, 128, framebuf.RGB565)

# This would create a picographics object with the framebuffer
graphics = picographics.PicoGraphics(128, 128, fb)

# This is how you could draw text with picographics
# But it will be in the default small font
graphics.text(10, 10, "Hello, world!")

# You need to display the framebuffer to the LCD using your display library
