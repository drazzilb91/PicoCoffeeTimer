import time
from machine import Pin, SPI, PWM,lightsleep, idle, deepsleep
from PicoLcd144 import LCD_1inch44

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

LCD = LCD_1inch44()

def sleepMode():
  key0 = Pin(15,Pin.IN,Pin.PULL_UP)
  while key0.value() == 1:
    print("sleeping")
    idle()
    # lightsleep(10000)
    deepsleep(10000)
  print("done sleeping")

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
    #color BRG
  LCD.fill(LCD.BLACK)

  LCD.show()

  LCD.fill_rect(15,40,75,12,LCD.YELLOW)
  LCD.rect(15,40,75,12,LCD.YELLOW)
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

  # Main loop
  while minutes < 1:

      # Check for button presses
      if key0.value() == 0:
          stopwatch.start()
      if key1.value() == 0:
          stopwatch.stop()
      if key2.value() == 0:
          stopwatch.reset()

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
      LCD.fill_rect(5,25,120,80,bgcolor)
      LCD.rect(5,25,120,80,bgcolor)
      # LCD.text(time_str, 52, 52, LCD.GREEN)
      LCD.text(time_str,45,62,LCD.WHITE)
      

      LCD.show()
      time.sleep(0.01)  # Update the display every 100 milliseconds


if __name__=='__main__':
  pwm = PWM(Pin(BL))
  pwm.freq(1000)
  pwm.duty_u16(32768)#max 65535

  key0 = Pin(15,Pin.IN,Pin.PULL_UP)
  key1 = Pin(17,Pin.IN,Pin.PULL_UP)
  key2 = Pin(2 ,Pin.IN,Pin.PULL_UP)
  key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)

  # Initialize the display
  splashScreen()

  stopwatchMode()
 
  print("Going to sleep now")
  LCD.fill(LCD.BLACK)
  LCD.text("Shutting Down", 20, 10, LCD.WHITE)
  LCD.show()
  LCD.fill(LCD.BLACK)
  LCD.show()
  
  sleepMode()