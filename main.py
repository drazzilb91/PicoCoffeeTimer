import time
from machine import Pin,SPI,PWM
from PicoLcd144 import LCD_1inch44

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

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


LCD = LCD_1inch44()

# Custom font data for numbers 0-9 (4x5 pixels per character)
custom_font_data = (
    0b11110,  # 0
    0b00100,  # 1
    0b10110,  # 2
    0b10100,  # 3
    0b01100,  # 4
    0b11000,  # 5
    0b11010,  # 6
    0b10101,  # 7
    0b11111,  # 8
    0b11101,  # 9
)

class CustomFont:
    def __init__(self, data, width, height):
        self.data = data
        self.width = width
        self.height = height

# Create an instance of the custom font
custom_font = CustomFont(custom_font_data, 4, 5)



if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535
    #color BRG
    LCD.fill(LCD.BLACK)

    LCD.show()

    LCD.fill_rect(15,40,75,12,LCD.YELLOW)
    LCD.rect(15,40,75,12,LCD.YELLOW)
    LCD.text("1in44-LCD",17,42,LCD.WHITE)

    LCD.fill_rect(15,60,75,12,LCD.BLUE)
    LCD.rect(15,60,75,12,LCD.BLUE)
    LCD.text("128x128Px ",17,62,LCD.WHITE)

    LCD.fill_rect(15,80,75,12,LCD.GREEN)
    LCD.rect(15,80,75,12,LCD.GREEN)
    LCD.text("ST7735S",17,82,LCD.WHITE)

    LCD.hline(5,5,120,LCD.GBLUE)
    LCD.hline(5,125,120,LCD.GBLUE)
    LCD.vline(5,5,120,LCD.GBLUE)
    LCD.vline(125,5,120,LCD.GBLUE)

    LCD.show()

    key0 = Pin(15,Pin.IN,Pin.PULL_UP)
    key1 = Pin(17,Pin.IN,Pin.PULL_UP)
    key2 = Pin(2 ,Pin.IN,Pin.PULL_UP)
    key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)

    time.sleep(5)
    LCD.fill(0xFFFF)

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
        LCD.text("Stopwatch", 20, 10, LCD.WHITE)
        LCD.text(time_str, 50, 50, LCD.GREEN)
        LCD.text("Start", 10, 100, LCD.WHITE)
        # LCD.write_data(custom_font.data)
        LCD.show()
        time.sleep(0.01)  # Update the display every 100 milliseconds

print("Going to sleep now")
LCD.fill(LCD.BLACK)
LCD.text("Shutting Down", 20, 10, LCD.WHITE)
LCD.show()