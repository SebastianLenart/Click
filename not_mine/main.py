from pynput import keyboard, mouse
from time import sleep

"""
1.) wsciskam klawisz windows
2.) paint
3.) wciskam enter

"""

controller = keyboard.Controller()
mouse_controller = mouse.Controller()
controller.press(keyboard.Key.cmd_l)  # windows
controller.release(keyboard.Key.cmd_l)
sleep(0.5)
controller.type("paint")
sleep(0.5)
controller.press(keyboard.Key.enter)
controller.release(keyboard.Key.enter)
sleep(1)

mouse_controller.position = (535, 492)
# mouse_controller.click(mouse.Button.left, 1)
mouse_controller.press(mouse.Button.left)
sleep(0.5)
for _ in range(10):
    mouse_controller.move(dx=10, dy=0)
    sleep(0.1)
sleep(0.5)
mouse_controller.release(mouse.Button.left)