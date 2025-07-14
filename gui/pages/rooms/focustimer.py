import tkinter as tk
import time
import threading

class FocusTimer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f7f9fb")  # Light background

        # Title
        tk.Label(self, text="⏳ Focus Timer", font=("Helvetica", 20, "bold"),
                 bg="#f7f9fb", fg="#2c3e50").pack(pady=(30, 10))

        # Time Entry Label
        tk.Label(self, text="⏱ Set Timer (minutes):", font=("Helvetica", 12),
                 bg="#f7f9fb", fg="#34495e").pack(pady=(10, 5))

        # Time Entry Field
        self.time_var = tk.IntVar(value=25)
        self.time_entry = tk.Entry(self, textvariable=self.time_var, width=5, font=("Helvetica", 12), justify="center")
        self.time_entry.pack(pady=(0, 15))

        # Start Button
        tk.Button(self, text="▶️ Start Timer", font=("Helvetica", 11),
                  bg="#27ae60", fg="white", activebackground="#1e8449",
                  command=self.start_timer).pack(pady=(5, 5), ipadx=8, ipady=2)

        # Stop Button
        tk.Button(self, text="⏹ Stop Timer", font=("Helvetica", 11),
                  bg="#e74c3c", fg="white", activebackground="#c0392b",
                  command=self.stop_timer).pack(pady=(0, 15), ipadx=8, ipady=2)

        # Countdown Display
        self.label = tk.Label(self, text="⏰ Time Remaining: --:--", font=("Helvetica", 14),
                              bg="#f7f9fb", fg="#2d3436")
        self.label.pack(pady=(0, 15))

        # Back Button
        tk.Button(self, text="⬅ Back to Reception", font=("Helvetica", 10),
                  bg="#dfe6e9", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)
        tk.Label(self, text="Made by Muhammad Asad Ullah", font=("Helvetica", 8), bg="#eafaf1", fg="gray").pack(side="bottom", pady=5)

        # Thread control
        self.timer_thread = None
        self.stop_event = threading.Event()

    def start_timer(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.stop_event.set()
            self.timer_thread.join()

        self.stop_event.clear()
        total_seconds = self.time_var.get() * 60

        def countdown():
            for sec in range(total_seconds, -1, -1):
                if self.stop_event.is_set():
                    break
                mins, s = divmod(sec, 60)
                time_str = f"{mins:02d}:{s:02d}"
                self.label.config(text=f"⏰ Time Remaining: {time_str}")
                time.sleep(1)
            else:
                self.label.config(text="✅ Focus session complete!")

        self.timer_thread = threading.Thread(target=countdown, daemon=True)
        self.timer_thread.start()

    def stop_timer(self):
        self.stop_event.set()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()
        self.label.config(text="⏹ Timer stopped.")
