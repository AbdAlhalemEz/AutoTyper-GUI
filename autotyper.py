import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

def start_typing():
    # Disable the button while typing
    start_button.config(state=tk.DISABLED)

    # Get user inputs
    text = text_box.get("1.0", tk.END).rstrip("\n")
    try:
        delay = float(delay_entry.get())
        prep_time = int(prep_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for delay and prep time.")
        start_button.config(state=tk.NORMAL)
        return

    # Run typing in a separate thread to keep GUI responsive
    def type_text():
        messagebox.showinfo("Get Ready", f"You have {prep_time} seconds to focus the chat window...")
        time.sleep(prep_time)

        for char in text:
            if char == "\n":
                pyautogui.press("enter")
            else:
                pyautogui.write(char)
            time.sleep(delay)
        
        messagebox.showinfo("Done", "✅ Finished typing!")
        start_button.config(state=tk.NORMAL)

    threading.Thread(target=type_text).start()

# Create GUI window
root = tk.Tk()
root.title("AutoTyper GUI")
root.geometry("500x400")

# Textbox
tk.Label(root, text="Enter your text:").pack()
text_box = tk.Text(root, height=10, width=60)
text_box.pack()

# Typing delay
tk.Label(root, text="Typing delay (seconds, e.g., 0.1):").pack()
delay_entry = tk.Entry(root)
delay_entry.insert(0, "0.1")
delay_entry.pack()

# Prep time
tk.Label(root, text="Prep time (seconds to switch window):").pack()
prep_entry = tk.Entry(root)
prep_entry.insert(0, "5")
prep_entry.pack()

# Start button
start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack(pady=10)

root.mainloop()
