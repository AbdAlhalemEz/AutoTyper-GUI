# AutoTyper GUI

AutoTyper GUI is a Python application that automatically types text letter by letter into any active window. It’s useful for chat apps that block pasting or for automating repetitive typing tasks.

---

## Features

- **Graphical Interface (GUI):** Easy-to-use textbox for entering your text.  
- **Adjustable Typing Delay:** Control the speed of typing per character.  
- **Prep Time:** Set a countdown before typing starts, giving you time to focus the target window.  
- **Multi-line Support:** Works with paragraphs and multiple lines of text.  
- **Standalone Executable:** Can be converted to a Windows `.exe` for use without Python installed.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AutoTyper-GUI.git
cd AutoTyper-GUI


2. Install dependencies:

pip install pyautogui


Note: tkinter comes built-in with Python on Windows, so no extra installation is needed for the GUI.

## Usage

Run the GUI script:

python autotyper_gui.py


1. Enter your text in the textbox.

2. Set typing delay (seconds per character).

3. Set prep time (seconds to switch to the target window).

4. Click Start Typing and quickly focus the window you want to type into.

# Convert to Windows Executable (Optional)

You can create a standalone .exe file using PyInstaller:

pip install pyinstaller
pyinstaller --onefile --noconsole autotyper_gui.py


The .exe will be in the dist folder.

It runs on any Windows machine without Python installed.

## Disclaimer

Use responsibly. Automating typing in chats or apps may violate the terms of service on certain platforms.


---

✅ **Next Steps:**  
1. Save this as `README.md` in your repository folder.  
2. Commit and push it to GitHub:

```bash
git add README.md
git commit -m "Add README for AutoTyper GUI"
git push
