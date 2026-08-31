import Functions.dynamic_mode_import
import Functions.ui
import Main.config as config
import Functions.oled_display as oled_display
import adafruit_ssd1306
import board
import busio

font = config.font
#oled display shi
WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

#import_modes_infos, imported_main_mode_files = Functions.dynamic_mode_import.import_modes()

oled_display.clear()
oled_display.display_text("Hello, World!", 0, font)
oled_display.show(oled)