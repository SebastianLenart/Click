from pynput import keyboard, mouse
from time import sleep
import json

"""
1.) wsciskam klawisz windows
2.) paint
3.) wciskam enter

"""


class Controller:
    """Control mouse and keyboard"""
    WAIT = 0.5

    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()

    def click_button(self, button):
        self.keyboard.press(button)
        self.keyboard.release(button)
        sleep(Controller.WAIT)

    def type(self, text):
        self.keyboard.type(text)
        sleep(Controller.WAIT)

    def hold_and_press(self, button_to_hold, button_to_press):
        with self.keyboard.press(button_to_hold):
            self.keyboard.press(button_to_press)

    def click_at_position(self, coordinate_x, coordinate_y):
        sleep(Controller.WAIT)
        self.mouse.position = (coordinate_x, coordinate_y)
        self.mouse.press(mouse.Button.left)

    def press_mouse_button(self, button=mouse.Button.left):
        self.mouse.press(button)

    def release_mouse_button(self, button=mouse.Button.left):
        self.mouse.release(button)

    def move_pointer(self, dx=0, dy=0):
        self.mouse.move(dx, dy)


class Process:
    def __init__(self, filename, controller):
        self.filename = filename
        self.steps = []
        self.controller = controller

    def load_steps(self):
        with open(self.filename) as file:
            self.steps = json.load(file)["steps"]

    def draw_line(self):
        for _ in range(10):
            self.controller.move_pointer(10, 5)
            sleep(0.1)
        sleep(0.5)
        self.controller.release_mouse_button()

    def start(self):
        options = {
            "Type": self.controller.type,
            "Click Button": lambda button: self.controller.click_button(getattr(keyboard.Key, button)),
            # "Hold and press": lambda button_to_hold, button_to_press: self.controller.hold_and_press(
            #     getattr(keyboard.Key, button_to_hold),
            #     getattr(keyboard.Key, button_to_press))
            "Click at position": self.controller.click_at_position,
            "Press mouse button": self.controller.press_mouse_button,
            "Draw line": self.draw_line

        }
        for step in self.steps:
            for key, value in step.items():
                options[key](**value)  # !!!!!


def main():
    controller = Controller()
    process = Process("actions.json", controller)
    process.load_steps()
    process.start()

    # controller = Controller()
    # controller.click_button(keyboard.Key.cmd_l)
    # sleep(0.5)
    # controller.type("paint")
    # sleep(0.5)
    # controller.click_button(keyboard.Key.enter)
    # sleep(1)
    # controller.click_at_position(535, 492)
    # sleep(0.5)
    # controller.press_mouse_butt    # for _ in range(10):
    #     #     controller.move_pointer(10, 5)
    #     #     sleep(0.1)
    #     # sleep(0.5)on()

    # controller.release_mouse_button()


if __name__ == "__main__":
    main()
