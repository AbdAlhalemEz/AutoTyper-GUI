# 🚀 Human-like AutoTyper

A sophisticated Python application that automates typing with human-like behavior patterns, making automated typing indistinguishable from real human typing. Features a modern GUI with customizable typing profiles and real-time progress tracking.

## ✨ Features

### 🎯 Human-like Typing Simulation
- **Variable Typing Speed**: Natural delay variations between keystrokes
- **Realistic Mistakes**: Character substitutions, omissions, repetitions with auto-correction
- **Natural Rhythm**: Longer pauses after punctuation, "thinking" pauses
- **Multiple Profiles**: Pre-configured typing personalities

### 👤 Typing Personalities
- **Slow and Careful** (30 WPM) - Methodical typing with few mistakes
- **Natural Typist** (45 WPM) - Balanced speed with occasional errors  
- **Fast Professional** (70 WPM) - Quick typing with more variance
- **Custom** - Fully customizable settings

### 🎨 Modern GUI
- **Clean, intuitive interface** with modern theme
- **Real-time progress tracking** with visual feedback
- **Smart placeholder text** and tooltips
- **Cancel functionality** for user control
- **Responsive design** that fits all controls perfectly

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- Required packages: `pyautogui`

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/autotyper.git
   cd autotyper
   ```

2. **Install dependencies**
   ```bash
   pip install pyautogui
   ```

3. **Run the application**
   ```bash
   python autotyper.py
   ```

## 📖 Usage
- **Enter Text**: Paste or type the text you want to automate in the text area  
- **Select Profile**: Choose a typing personality or create custom settings  
- **Configure Options**:
  - Enable/disable human-like features (mistakes, pauses, variance)
  - Set preparation time to switch to target window  
- **Start Typing**: Click "Start Human-like Typing" and switch to your target application  
- **Monitor Progress**: Watch real-time progress with character count and percentage  

## 🎛️ Custom Settings
- **Words Per Minute**: Control overall typing speed (30-100+ WPM)  
- **Mistake Chance**: Adjust how often errors occur (0-100%)  
- **Pause Chance**: Control frequency of natural pauses  
- **Human Features**: Toggle individual human-like behaviors  

## 🔧 Technical Details
**Built With**  
- Python 3 - Core programming language  
- Tkinter - GUI framework  
- PyAutoGUI - Cross-platform automation  
- Threading - Non-blocking UI operations  

**File Structure**
```bash
autotyper/
├── autotyper.py      # Main application file
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## 🎯 Human Typing Algorithms
- **Variable Speed Calculation**
  - Base speed calculated from WPM (Words Per Minute)  
  - Random variance applied to each keystroke  
  - Longer pauses after sentences and punctuation  
  - Natural "thinking" pauses at random intervals  

- **Mistake Simulation**
  - Substitution: Wrong characters (common keyboard errors)  
  - Omission: Skipped characters  
  - Repetition: Double-typed characters  
  - Auto-correction: Realistic backspacing and correction  

- **Natural Rhythm**
  - Sentence-end pauses: 2-4x normal delay  
  - Clause pauses: 1.5-2.5x normal delay  
  - Word-boundary variations: ±20% speed changes  
  - Random thinking pauses: 0.5-2.0 seconds  

## ⚠️ Important Notes
- Administrator Rights: May require admin privileges on some systems  
- Security Software: Some antivirus programs may flag automation tools  
- Target Application: Ensure your target window is accessible and focused  
- Test First: Always test with small text before long automation sessions  
- Window Focus: The application will type wherever your cursor is focused after the preparation time  

## 🚨 Disclaimer
This tool is intended for legitimate purposes only:
- Personal productivity automation  
- Testing and development  
- Educational purposes  
- Accessibility assistance  

Users are responsible for complying with terms of service of target applications and local laws. The developers are not responsible for misuse.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes  
- New features  
- Documentation improvements  
- UI/UX enhancements  
- Additional typing profiles  

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/autotyper.git
cd autotyper

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pyautogui
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support
If you encounter any issues:
1. **Check Existing Issues**: Look through the Issues page for existing solutions  
2. **Create New Issue**: Include:  
   - Detailed description of the problem  
   - Steps to reproduce  
   - Your operating system and version  
   - Python version  
   - Error messages (if any)  

## 🙏 Acknowledgments
- PyAutoGUI for cross-platform automation capabilities  
- Tkinter for the robust GUI framework  
- The Python community for continuous inspiration and support  

⭐ Star this repo if you find it helpful!  

🐛 Found a bug? Please open an issue with detailed steps to reproduce.  
💡 Have an idea? We'd love to hear your suggestions for new features!
