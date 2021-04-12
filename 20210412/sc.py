import time
import keyboard
from PIL import ImageGrab
def screenct():
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    image = ImageGrab.grab()
    image.save("image{}.png".format(cur_time))
keyboard.add_hotkey("F8", screenct)
keyboard.wait("esc")