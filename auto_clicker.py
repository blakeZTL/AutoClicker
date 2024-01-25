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

def set_hotkey():
    """
    Sets the hotkey to the user specified key.
    """
    global hotkey
    new_hotkey = entry_hotkey.get()
    try:
        # Remove the old hotkey
        if hotkey:
            keyboard.remove_hotkey(hotkey)
        # Add the new hotkey
        hotkey = keyboard.add_hotkey(new_hotkey, on_toggle_key)
    except ValueError:
        print("Invalid key. Please enter a valid key.")

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

# Set base width and height
base_width = 200
base_height = 150
root.minsize(base_width, base_height)
wider_width = int(base_width * 1.5)
root.geometry(f"{wider_width}x{base_height}")

# Interval input
tk.Label(root, text="Interval (seconds):").pack()
entry_interval = tk.Entry(root)
entry_interval.pack()

# Hotkey input
tk.Label(root, text="Enter hotkey (e.g., F5):").pack()
entry_hotkey = tk.Entry(root)
entry_hotkey.pack()

# Set hotkey button
set_hotkey_button = tk.Button(root, text="Set Hotkey", command=set_hotkey)
set_hotkey_button.pack()

# Instructions label
instructions = tk.Label(root, text="Set a hotkey and press it to toggle auto clicker")
instructions.pack()

# Initialize hotkey variable
hotkey = None

# Run the application
root.mainloop()
