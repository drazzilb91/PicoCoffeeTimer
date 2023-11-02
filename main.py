"""
This script is for a coffee timer project using a Raspberry Pi Pico and a 1.44 inch LCD display.
It contains functions for drawing characters and strings on the LCD framebuffer, as well as a stopwatch class.
The main function initializes the display, shows a splash screen, and switches between stopwatch and sleep modes based on button presses.
"""
import time
from machine import Pin, SPI, PWM, idle
from PicoLcd144 import LCD_1inch44
from customFont import bitmaps, bitmaps_dark

# Define the SPI pins
BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

# Create a new LCD instance
LCD = LCD_1inch44()

# Define the button pins
key0 = Pin(15,Pin.IN,Pin.PULL_UP)
key1 = Pin(17,Pin.IN,Pin.PULL_UP)
key2 = Pin(2 ,Pin.IN,Pin.PULL_UP)
key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)

# Define the interrupt handler
def button_handler(pin):
    print("Button pressed!")
    global awake_flag
    awake_flag = True

# Attach the interrupt handler to the button pin
key0.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
key1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
key2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
key3.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Function to draw a character on the LCD framebuffer
def draw_char(lcd_fb, x, y, char, color):
    if color == LCD.WHITE:
        char_fb = bitmaps[char] 
        lcd_fb.blit(char_fb, x, y, LCD.BLACK)
    else:
        char_fb = bitmaps_dark[char]
        lcd_fb.blit(char_fb, x, y, LCD.WHITE)

    # Use the blit method to draw the character framebuffer onto the LCD framebuffer
    # print("Is LCD.WHITE?" + str( color == LCD.WHITE))
    # lcd_fb.blit(char_fb, x, y, LCD.WHITE if color == LCD.BLACK else LCD.BLACK)
    # lcd_fb.blit(char_fb, x, y, LCD.BLACK)

# Function to draw a string on the LCD framebuffer
def draw_string(lcd_fb, x, y, string, color):
    for i, char in enumerate(string):
        draw_char(lcd_fb, x + i * 18, y, char, color)  # 18 is the character width including space

# Function to manage the sleep mode
def sleepMode():
  global awake_flag 
  awake_flag = False

  # Turn off the LCD display
  LCD.display_off()

  # Turn off the backlight
  pwm = PWM(Pin(BL))
  pwm.freq(1000)
  pwm.duty_u16(0)#max 65535

  while awake_flag is False:
    idle()

  print("done sleeping")

  # Turn on the backlight
  pwm = PWM(Pin(BL))
  pwm.freq(1000)
  pwm.duty_u16(32768)#max 65535

  # Turn on the LCD display
  LCD.display_on()

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.ticks_ms()
            self.is_running = True

    def stop(self):
        if self.is_running:
            self.elapsed_time = self.elapsed_time + time.ticks_diff(time.ticks_ms(), self.start_time)
            self.is_running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def get_elapsed_time(self):
        if self.is_running:
            return self.elapsed_time + time.ticks_diff(time.ticks_ms(), self.start_time)
        return self.elapsed_time

def splashScreen():
  #color order is BGR
  LCD.fill(LCD.BLACK)


  LCD.show()

  LCD.fill_rect(15,40,75,12,LCD.CYAN)
  LCD.rect(15,40,75,12,LCD.CYAN)
  LCD.text("Offside ",17,42,LCD.WHITE)

  LCD.fill_rect(15,60,75,12,LCD.BLUE)
  LCD.rect(15,60,75,12,LCD.BLUE)
  LCD.text("Espresso ",17,62,LCD.WHITE)

  LCD.fill_rect(15,80,75,12,LCD.GREEN)
  LCD.rect(15,80,75,12,LCD.GREEN)
  LCD.text("Bar",17,82,LCD.WHITE)

  LCD.hline(5,5,120,LCD.GBLUE)
  LCD.hline(5,125,120,LCD.GBLUE)
  LCD.vline(5,5,120,LCD.GBLUE)
  LCD.vline(125,5,120,LCD.GBLUE)

  LCD.show()
  time.sleep(2)


def stopwatchMode():
   # Initialize the stopwatch
  stopwatch = Stopwatch()

  # Initialize the elapsed time
  minutes = 0
  seconds = 0

  temp_num = 0
  # Main loop
  # while minutes < 1:
  while seconds < 10:

      # Check for button presses
      if key0.value() == 0:
          stopwatch.start()
      if key1.value() == 0:
          stopwatch.stop()
      if key2.value() == 0:
          stopwatch.reset()
      if key3.value() == 0:
          LCD.set_rotation(temp_num)
          if temp_num == 3:
            temp_num = 0
          else:
            temp_num = temp_num + 1

      # Calculate and format elapsed time
      elapsed = stopwatch.get_elapsed_time() // 1000  # Convert to seconds
      minutes = elapsed // 60
      seconds = elapsed % 60
      time_str = f"{minutes:02}:{seconds:02}"

      # Clear the display and show the elapsed time
      LCD.fill(LCD.BLACK)
      LCD.text("Coffee Timer", 20, 10, LCD.WHITE)

      if elapsed < 20:
        bgcolor = LCD.RED
      elif elapsed < 28:
        bgcolor = LCD.YELLOW
      elif elapsed < 34:
        bgcolor = LCD.GREEN
      elif elapsed < 36:
        bgcolor = LCD.YELLOW
      elif elapsed < 38:
         bgcolor = LCD.RED
      elif elapsed < 45:
        bgcolor = LCD.RED
      else:
        bgcolor = LCD.BLACK
      # print(bgcolor)

      if bgcolor == LCD.YELLOW:
        text_color = LCD.BLACK

      else:
        text_color = LCD.WHITE

      LCD.fill_rect(5,25,120,80,bgcolor)
      LCD.rect(5,25,120,80,bgcolor)
      # LCD.text(time_str, 52, 52, LCD.GREEN)
      # LCD.text(time_str,45,62,text_color)
      draw_string(LCD,21, 53, time_str, text_color)

      LCD.show()
      time.sleep(0.1)  # Update the display every 100 milliseconds

if __name__=='__main__':
  # Turn on the backlight
  pwm = PWM(Pin(BL))
  pwm.freq(1000)
  pwm.duty_u16(32768)#max 65535

  # Initialize the display
  splashScreen()

  # Last-ditch attempt to escape the program by pressing buttons 0 and 3 simultaneously
  while not (key0.value() == 0 and key3.value() == 0):
    print("Main: Switching to stopwatch mode")
    stopwatchMode()

    print("Main: Switching to sleep mode")
    sleepMode()
