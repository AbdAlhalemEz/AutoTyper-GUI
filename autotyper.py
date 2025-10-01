import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import time
import threading
import random
import string

class AutoTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoTyper - Human-like Text Automation")
        self.root.geometry("650x700")  # Increased window size
        self.root.resizable(True, True)
        
        # Set modern theme colors
        self.bg_color = "#f5f6fa"
        self.accent_color = "#4834d4"
        self.text_color = "#2c3e50"
        self.success_color = "#27ae60"
        
        self.root.configure(bg=self.bg_color)
        
        # Initialize variables
        self.is_typing = False
        self.cancel_flag = False
        
        # Human typing patterns
        self.setup_typing_profiles()
        self.setup_ui()
        
    def setup_typing_profiles(self):
        # Different typing speed profiles (words per minute)
        self.typing_profiles = {
            "Slow and Careful": {
                "wpm": 30,
                "delay_variance": 0.3,
                "mistake_chance": 0.005,
                "pause_chance": 0.1
            },
            "Natural Typist": {
                "wpm": 45,
                "delay_variance": 0.2,
                "mistake_chance": 0.01,
                "pause_chance": 0.15
            },
            "Fast Professional": {
                "wpm": 70,
                "delay_variance": 0.1,
                "mistake_chance": 0.02,
                "pause_chance": 0.08
            },
            "Custom": {
                "wpm": 45,
                "delay_variance": 0.2,
                "mistake_chance": 0.01,
                "pause_chance": 0.15
            }
        }
        
    def setup_ui(self):
        # Create main frame with scrollbar
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Header
        header_frame = tk.Frame(main_container, bg=self.accent_color, height=80)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🚀 Human-like AutoTyper", 
                              font=("Arial", 20, "bold"), 
                              fg="white", bg=self.accent_color)
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(header_frame, 
                                 text="Type like a real human - with natural variations and patterns", 
                                 font=("Arial", 10), 
                                 fg="#dfe6e9", bg=self.accent_color)
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(main_container, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text input section
        text_frame = tk.LabelFrame(main_frame, text="📝 Text to Type", 
                                  font=("Arial", 11, "bold"),
                                  bg=self.bg_color, fg=self.text_color,
                                  padx=10, pady=10)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Add scrollbar to text box
        text_container = tk.Frame(text_frame, bg=self.bg_color)
        text_container.pack(fill=tk.BOTH, expand=True)
        
        self.text_box = tk.Text(text_container, height=8, 
                               font=("Arial", 10),
                               relief=tk.FLAT, bg="white",
                               wrap=tk.WORD)
        
        text_scrollbar = ttk.Scrollbar(text_container, orient=tk.VERTICAL, command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=text_scrollbar.set)
        
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add placeholder text
        self.text_box.insert("1.0", "Enter the text you want to automate here...\n\nTip: The more text, the more natural it will feel!")
        self.text_box.bind("<FocusIn>", self.clear_placeholder)
        self.text_box.bind("<FocusOut>", self.restore_placeholder)
        
        # Typing Profile Section
        profile_frame = tk.LabelFrame(main_frame, text="👤 Typing Style", 
                                     font=("Arial", 11, "bold"),
                                     bg=self.bg_color, fg=self.text_color,
                                     padx=10, pady=10)
        profile_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Profile selection
        profile_top_frame = tk.Frame(profile_frame, bg=self.bg_color)
        profile_top_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(profile_top_frame, text="Select typing personality:", 
                font=("Arial", 9, "bold"), bg=self.bg_color, fg=self.text_color).pack(side=tk.LEFT)
        
        self.profile_var = tk.StringVar(value="Natural Typist")
        profile_combo = ttk.Combobox(profile_top_frame, textvariable=self.profile_var,
                                    values=list(self.typing_profiles.keys()),
                                    state="readonly", width=20)
        profile_combo.pack(side=tk.LEFT, padx=(10, 0))
        profile_combo.bind("<<ComboboxSelected>>", self.on_profile_change)
        
        # Custom settings frame (initially hidden)
        self.custom_frame = tk.Frame(profile_frame, bg=self.bg_color)
        
        # Create a grid for custom settings with better spacing
        tk.Label(self.custom_frame, text="Words per minute:", 
                font=("Arial", 8, "bold"), bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, sticky=tk.W, padx=(0, 15))
        self.wpm_var = tk.StringVar(value="45")
        wpm_entry = tk.Entry(self.custom_frame, textvariable=self.wpm_var, width=10, font=("Arial", 9))
        wpm_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 15), pady=(2, 5))
        
        tk.Label(self.custom_frame, text="Mistake chance (%):", 
                font=("Arial", 8, "bold"), bg=self.bg_color, fg=self.text_color).grid(row=0, column=1, sticky=tk.W, padx=(0, 15))
        self.mistake_var = tk.StringVar(value="1")
        mistake_entry = tk.Entry(self.custom_frame, textvariable=self.mistake_var, width=10, font=("Arial", 9))
        mistake_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 15), pady=(2, 5))
        
        tk.Label(self.custom_frame, text="Pause chance (%):", 
                font=("Arial", 8, "bold"), bg=self.bg_color, fg=self.text_color).grid(row=0, column=2, sticky=tk.W)
        self.pause_var = tk.StringVar(value="15")
        pause_entry = tk.Entry(self.custom_frame, textvariable=self.pause_var, width=10, font=("Arial", 9))
        pause_entry.grid(row=1, column=2, sticky=tk.W, pady=(2, 5))
        
        # Human-like features - arranged in a grid for better layout
        features_frame = tk.Frame(profile_frame, bg=self.bg_color)
        features_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.correction_var = tk.BooleanVar(value=True)
        correction_cb = tk.Checkbutton(features_frame, text="Auto-correct mistakes", 
                      variable=self.correction_var, bg=self.bg_color,
                      font=("Arial", 9))
        correction_cb.grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        
        self.pauses_var = tk.BooleanVar(value=True)
        pauses_cb = tk.Checkbutton(features_frame, text="Natural pauses", 
                      variable=self.pauses_var, bg=self.bg_color,
                      font=("Arial", 9))
        pauses_cb.grid(row=0, column=1, sticky=tk.W, padx=(0, 20))
        
        self.variance_var = tk.BooleanVar(value=True)
        variance_cb = tk.Checkbutton(features_frame, text="Typing speed variance", 
                      variable=self.variance_var, bg=self.bg_color,
                      font=("Arial", 9))
        variance_cb.grid(row=0, column=2, sticky=tk.W)
        
        # Settings frame
        settings_frame = tk.Frame(main_frame, bg=self.bg_color)
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Prep time setting
        prep_frame = tk.Frame(settings_frame, bg=self.bg_color)
        prep_frame.pack(fill=tk.X, pady=5)
        
        prep_label_frame = tk.Frame(prep_frame, bg=self.bg_color)
        prep_label_frame.pack(fill=tk.X)
        
        tk.Label(prep_label_frame, text="⏰  Preparation time (seconds):", 
                font=("Arial", 9, "bold"), bg=self.bg_color, fg=self.text_color).pack(side=tk.LEFT)
        
        self.prep_entry = tk.Entry(prep_label_frame, font=("Arial", 10),
                                  relief=tk.FLAT, bg="white", width=10)
        self.prep_entry.insert(0, "5")
        self.prep_entry.pack(side=tk.LEFT, padx=(10, 0))
        
        tk.Label(prep_frame, text="Time to switch to target window", 
                font=("Arial", 8), bg=self.bg_color, fg="#7f8c8d").pack(anchor=tk.W, pady=(2, 0))
        
        # Progress section
        self.progress_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.progress_frame.pack(fill=tk.X, pady=(10, 10))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='determinate')
        self.status_label = tk.Label(self.progress_frame, text="Ready to type!", 
                                    font=("Arial", 9), bg=self.bg_color, fg=self.text_color)
        
        # Button frame - centered with proper spacing
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=15)
        
        # Center the buttons
        button_container = tk.Frame(button_frame, bg=self.bg_color)
        button_container.pack(expand=True)
        
        self.start_button = tk.Button(button_container, text="🎯 Start Human-like Typing", 
                                     font=("Arial", 11, "bold"),
                                     bg=self.success_color, fg="white",
                                     relief=tk.FLAT, padx=25, pady=12,
                                     command=self.start_typing)
        self.start_button.pack(side=tk.LEFT, padx=(0, 15))
        
        self.cancel_button = tk.Button(button_container, text="❌ Cancel", 
                                      font=("Arial", 10),
                                      bg="#e74c3c", fg="white",
                                      relief=tk.FLAT, padx=25, pady=10,
                                      command=self.cancel_typing,
                                      state=tk.DISABLED)
        self.cancel_button.pack(side=tk.LEFT)
        
        # Footer with tips
        footer_frame = tk.Frame(main_container, bg=self.bg_color)
        footer_frame.pack(fill=tk.X, pady=10)
        
        tips = [
            "💡 Different profiles simulate different typing styles and speeds",
            "💡 Natural pauses make the typing look more human",
            "💡 Mistakes with corrections add authenticity to the typing",
            "💡 Longer texts work better for natural rhythm"
        ]
        
        for tip in tips:
            tip_label = tk.Label(footer_frame, text=tip, font=("Arial", 8), 
                    bg=self.bg_color, fg="#7f8c8d")
            tip_label.pack(anchor=tk.W)
    
    def on_profile_change(self, event):
        profile = self.profile_var.get()
        if profile == "Custom":
            self.custom_frame.pack(fill=tk.X, pady=(10, 0))
        else:
            self.custom_frame.pack_forget()
    
    def clear_placeholder(self, event):
        if "Enter the text you want to automate here" in self.text_box.get("1.0", "end-1c"):
            self.text_box.delete("1.0", tk.END)
    
    def restore_placeholder(self, event):
        if not self.text_box.get("1.0", "end-1c").strip():
            self.text_box.insert("1.0", "Enter the text you want to automate here...\n\nTip: The more text, the more natural it will feel!")
    
    def calculate_typing_parameters(self):
        profile_name = self.profile_var.get()
        
        if profile_name == "Custom":
            try:
                wpm = int(self.wpm_var.get())
                mistake_chance = int(self.mistake_var.get()) / 100.0
                pause_chance = int(self.pause_var.get()) / 100.0
                delay_variance = 0.2
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for custom settings")
                return None
        else:
            profile = self.typing_profiles[profile_name]
            wpm = profile["wpm"]
            mistake_chance = profile["mistake_chance"]
            pause_chance = profile["pause_chance"]
            delay_variance = profile["delay_variance"]
        
        # Calculate base delay from WPM (words per minute)
        # Average word length in English is ~5 characters + 1 space
        chars_per_minute = wpm * 6
        base_delay = 60.0 / chars_per_minute
        
        return {
            "base_delay": base_delay,
            "delay_variance": delay_variance,
            "mistake_chance": mistake_chance if self.correction_var.get() else 0,
            "pause_chance": pause_chance if self.pauses_var.get() else 0,
            "speed_variance": self.variance_var.get()
        }
    
    def human_like_delay(self, base_delay, variance, char, last_char_was_space):
        # Add random variance to delay
        if self.variance_var.get():
            delay = base_delay * random.uniform(1 - variance, 1 + variance)
        else:
            delay = base_delay
        
        # Longer delay after punctuation and spaces
        if char in '.!?':
            delay *= random.uniform(2.0, 4.0)  # Natural pause after sentences
        elif char in ',;:':
            delay *= random.uniform(1.5, 2.5)  # Short pause after clauses
        elif last_char_was_space:
            delay *= random.uniform(0.8, 1.2)  # Slight variance after spaces
        
        # Occasional longer pauses (thinking time)
        if self.pauses_var.get() and random.random() < 0.02:  # 2% chance for a thinking pause
            delay += random.uniform(0.5, 2.0)
        
        return max(delay, 0.01)  # Minimum delay to avoid zero
    
    def make_mistake(self, char):
        """Simulate common typing mistakes"""
        if not char.isalnum():
            return None
            
        mistake_type = random.choice(['substitution', 'omission', 'repetition', 'transposition'])
        
        if mistake_type == 'substitution':
            # Type a nearby key instead
            if char.isalpha():
                return random.choice(string.ascii_lowercase)
            elif char.isdigit():
                return random.choice(string.digits)
        elif mistake_type == 'omission':
            # Skip the character
            return ''
        elif mistake_type == 'repetition':
            # Type the character twice
            return char + char
        elif mistake_type == 'transposition':
            # This will be handled in the main loop for two characters
            pass
            
        return None
    
    def simulate_backspace(self, count=1):
        """Simulate backspacing with human-like timing"""
        for i in range(count):
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.15))
    
    def update_progress(self, show=True):
        if show:
            self.progress_bar.pack(fill=tk.X, pady=(0, 5))
            self.status_label.pack(fill=tk.X)
        else:
            self.progress_bar.pack_forget()
            self.status_label.pack_forget()
    
    def start_typing(self):
        if self.is_typing:
            return
            
        # Get user inputs
        text = self.text_box.get("1.0", tk.END).rstrip("\n")
        
        # Check if it's placeholder text
        if "Enter the text you want to automate here" in text:
            messagebox.showwarning("Empty Text", "Please enter some text to type!")
            return
            
        if not text.strip():
            messagebox.showwarning("Empty Text", "Please enter some text to type!")
            return
        
        try:
            prep_time = int(self.prep_entry.get())
            typing_params = self.calculate_typing_parameters()
            if typing_params is None:
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for prep time.")
            return
        
        # Update UI
        self.is_typing = True
        self.cancel_flag = False
        self.start_button.config(state=tk.DISABLED, text="⏳ Starting...")
        self.cancel_button.config(state=tk.NORMAL)
        self.update_progress(True)
        self.progress_bar.config(maximum=len(text), value=0)
        
        # Run typing in a separate thread
        threading.Thread(target=self.type_text, args=(text, typing_params, prep_time), daemon=True).start()
    
    def cancel_typing(self):
        self.cancel_flag = True
        self.status_label.config(text="Cancelling...")
    
    def type_text(self, text, params, prep_time):
        try:
            # Countdown phase
            for i in range(prep_time, 0, -1):
                if self.cancel_flag:
                    self.finish_typing(cancelled=True)
                    return
                    
                self.status_label.config(text=f"⏳ Switching to target window... {i}s")
                time.sleep(1)
            
            if self.cancel_flag:
                self.finish_typing(cancelled=True)
                return
            
            # Typing phase
            total_chars = len(text)
            typed_chars = 0
            i = 0
            
            while i < len(text):
                if self.cancel_flag:
                    break
                
                char = text[i]
                last_char_was_space = (i > 0 and text[i-1] == ' ')
                
                # Calculate human-like delay for this character
                delay = self.human_like_delay(params["base_delay"], params["delay_variance"], char, last_char_was_space)
                
                # Simulate occasional mistakes
                made_mistake = False
                if (params["mistake_chance"] > 0 and char.isalnum() and 
                    random.random() < params["mistake_chance"]):
                    
                    mistake = self.make_mistake(char)
                    if mistake is not None:
                        made_mistake = True
                        pyautogui.write(mistake)
                        time.sleep(delay)
                        
                        # Correct the mistake after a short pause
                        if mistake != '' and self.correction_var.get():
                            time.sleep(random.uniform(0.2, 0.5))  # Realization pause
                            self.simulate_backspace(len(mistake))
                            pyautogui.write(char)
                
                if not made_mistake:
                    if char == "\n":
                        pyautogui.press("enter")
                    else:
                        pyautogui.write(char)
                
                typed_chars += 1
                progress = (typed_chars / total_chars) * 100
                self.status_label.config(text=f"⌨️  Typing... {typed_chars}/{total_chars} characters ({progress:.1f}%)")
                self.progress_bar.config(value=typed_chars)
                
                time.sleep(delay)
                i += 1
            
            if not self.cancel_flag:
                self.finish_typing(success=True)
            else:
                self.finish_typing(cancelled=True)
                
        except Exception as e:
            self.finish_typing(error=str(e))
    
    def finish_typing(self, success=False, cancelled=False, error=None):
        self.is_typing = False
        self.cancel_flag = False
        
        # Update UI in main thread
        self.root.after(0, self._update_ui_after_typing, success, cancelled, error)
    
    def _update_ui_after_typing(self, success, cancelled, error):
        self.start_button.config(state=tk.NORMAL, text="🎯 Start Human-like Typing")
        self.cancel_button.config(state=tk.DISABLED)
        self.update_progress(False)
        
        if success:
            self.status_label.config(text="✅ Finished typing naturally!", fg=self.success_color)
            messagebox.showinfo("Success", "✅ Finished typing your text with human-like patterns!")
        elif cancelled:
            self.status_label.config(text="⏹️  Typing cancelled", fg="#e74c3c")
        elif error:
            self.status_label.config(text="❌ Error occurred", fg="#e74c3c")
            messagebox.showerror("Error", f"Something went wrong:\n{error}")

def main():
    root = tk.Tk()
    app = AutoTyper(root)
    root.mainloop()

if __name__ == "__main__":
    main()
