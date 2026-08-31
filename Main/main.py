import Functions.dynamic_mode_import
import Functions.ui
import Main.config as config
import Functions.oled_display as oled_display

font = config.font

#import_modes_infos, imported_main_mode_files = Functions.dynamic_mode_import.import_modes()

oled_display.clear()
oled_display.display_text("Hello, World!", 0, font)
oled_display.show()