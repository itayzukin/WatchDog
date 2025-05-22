import user.stream_server.global_vars as gv
import threading
import keyboard
import pyautogui

class InputExecutionConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)

    def run(self):
        with True:
            with gv.input_condition:
                while not gv.input_queue:
                    gv.input_condition.wait()
                key = gv.input_queue.pop()
                key = key.strip().split()
                if key[0].upper() == 'KEYBOARD':
                    keyboard.press(key[1])
                if key[0].upper() == 'MOUSE':
                    self.handle_command(key)

    def handle_command(self, key):
        if key[1].upper() == "MOVE":
            x = int(key[2])
            y = int(key[3])
            pyautogui.moveTo(x, y)
        elif key[1] == "CLICK":
            pyautogui.click()
        elif key[1] == "RIGHT_CLICK":
            pyautogui.click(button='right')
        elif key[1] == "DOUBLE_CLICK":
            pyautogui.doubleClick()
        elif key[1] == "DRAG":
            x = int(key[1])
            y = int(key[2])
            pyautogui.dragTo(x, y, duration=0.5)
        elif key[1] == "SCROLL":
            amount = int(key[1])
            pyautogui.scroll(amount)
                
                