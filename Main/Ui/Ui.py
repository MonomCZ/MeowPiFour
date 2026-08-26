#testing for now
import Functions.oled_display as oled_display
import time

while True:
    oled_display.clear()
    oled_display.display_temperature()
    oled_display.show()
    time.sleep(5)
