import pyautogui
import tkinter as tk
from threading import Thread
import keyboard
import time

running = False


def auto_clicker(interval):
    global running
    running = True
    while running:
        pyautogui.click()
        time.sleep(interval)


def on_toggle_key():
    global running
    if running:
        running = False
    else:
        interval = float(entry_interval.get())
        Thread(target=auto_clicker, args=(interval,)).start()


# GUI setup
root = tk.Tk()
root.title("Python Auto Clicker")

# Interval input
tk.Label(root, text="Interval (seconds):").pack()
entry_interval = tk.Entry(root)
entry_interval.pack()

# Instructions label
instructions = tk.Label(root, text="Press F5 to toggle auto clicker")
instructions.pack()

# Set the keybind
keyboard.add_hotkey("F5", on_toggle_key)

# Run the application
root.mainloop()
