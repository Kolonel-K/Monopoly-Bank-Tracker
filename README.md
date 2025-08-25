## 🏦 Monopoly Bank (Tkinter)
A Python project using Tkinter that acts as a digital bank for Monopoly. This app helps track each player’s money in real time, preventing manual errors or cheating. Players can register at the start, receive a starting balance, and update their money through simple add/deduct actions.

## ✨ Features
- 🎮 **Player Setup:** Enter number of players and names at the start.
- 💰 **Automatic Balance Tracking:** Each player starts with a set amount of money (default: 30,000).
- ➕ **Add or Deduct Money:** Quickly update player balances with a dropdown menu and entry field.
- 📊 **Real-Time Updates:** Balances update dynamically on-screen.
- 🎨 **Modern GUI:** Simple dark-themed interface built with Tkinter.

## ⚙️ Installation & Setup
1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/monopoly-bank.git
cd monopoly-bank
```
2. Run the program
```bash
python monopoly_bank.py
No extra dependencies required — only Python’s built-in tkinter library.
```

## 🚀 Usage
- Launch the program with python monopoly_bank.py.
- Enter the number of players.
- Type and submit the player names.
- The game screen will open showing player names and their balances.
- Select a player, choose an action (Add Money or Deduct Money), and enter the amount.
- Click Enter to update balances in real time.

## 🔧 Customization
**Starting Balance:** By default, players start with 30,000. You can change this by editing:
```python
start_money = 30000
```
**Themes/Colors:** 
- Background and text colors are set to a dark theme (#1f1f1f background, #dedede text).
- Update in the .configure(background=...) or Label/Entry/OptionMenu widgets.

## 📚 Learning Outcomes
- Design a responsive GUI using Tkinter components.
- Implement event-driven programming and callback functions.
- Manage and update dynamic data structures in Python.
- Build practical, real-time apps for user interaction.
- Strengthen code reliability and user experience with error prevention.
  
## 📌 Future Improvements
- Save/load game progress.
- Adjustable starting balances per player.
- Transaction history tracking.
- Improved layout and responsive design.

## 🧑‍💻 Author
Developed by _Kanav Veer Singh_ – A software engineering student working on Python, data storage, and GUI development.
