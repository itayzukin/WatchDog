import user.stream_server.global_vars as gv
import threading
import keyboard
import pyautogui

class InputExecutionConsumerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)

    def run(self):
        while True:
            with gv.input_condition:
                while not gv.input_queue:
                    gv.input_condition.wait()
                key_string = gv.input_queue.pop(0)
            self.process_key(key_string)

    def process_key(self, key_string):
        key = key_string.strip().split()
        if not key:
            return

        match key[0].upper():
            case 'KEYBOARD':
                keyboard.press(key[1])
            case 'MOUSE':
                self.handle_mouse_command(key)

    def handle_mouse_command(self, key):
        match key[1].upper():
            case "MOVE" if len(key) >= 4:
                x, y = int(key[2]), int(key[3])
                pyautogui.moveTo(x, y)
            case "LEFT_CLICK":
                pyautogui.click()
            case "RIGHT_CLICK":
                pyautogui.click(button='right')
            case "DRAG" if len(key) >= 4:
                x, y = int(key[2]), int(key[3])
                pyautogui.dragTo(x, y, duration=0.5)
            case "SCROLL" if len(key) >= 3:
                amount = int(key[2])
                pyautogui.scroll(amount)
