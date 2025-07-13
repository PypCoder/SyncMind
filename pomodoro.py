import tkinter as tk
import time
import threading

class PomodoroTimer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.time_left = 25 * 60
        self.running = False

        self.label = tk.Label(self, text="25:00", font=("Arial", 30), fg="red")
        self.label.pack(pady=20)

        self.start_button = tk.Button(self, text="▶ Start", command=self.start_timer)
        self.start_button.pack()

        self.reset_button = tk.Button(self, text="🔄 Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

    def update_display(self):
        mins = self.time_left // 60
        secs = self.time_left % 60
        self.label.config(text=f"{mins:02d}:{secs:02d}")

    def countdown(self):
        while self.running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.update_display()
        if self.time_left == 0:
            self.label.config(text="⏰ Time's up!", fg="green")

    def start_timer(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.countdown, daemon=True).start()

    def reset_timer(self):
        self.running = False
        self.time_left = 25 * 60
        self.update_display()
        self.label.config(fg="red")
