import tkinter as tk
from pomodoro import PomodoroTimer

class SubhanRoom(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="🧠 Subhan’s Productivity Room", font=("Arial", 18, "bold")).pack(pady=10)

        # Embed the mini Pomodoro tool
        PomodoroTimer(self).pack()
