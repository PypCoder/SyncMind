import tkinter as tk
from tkinter import ttk

class SyncMindApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧠 SyncMind — Your Mind’s Co-Pilot")
        self.geometry("900x620")
        self.configure(bg="#e9f1f7")  # Light background

        style = ttk.Style()
        style.configure("TNotebook", background="#e9f1f7", padding=10)
        style.configure("TNotebook.Tab", font=('Arial', 11, 'bold'))

        # Notebook for sections
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        # Define frames
        self.the_pulse_frame = tk.Frame(self.notebook, bg="#ffffff")
        self.autopilot_frame = tk.Frame(self.notebook, bg="#ffffff")
        self.rooms_frame = tk.Frame(self.notebook, bg="#ffffff")

        self.notebook.add(self.the_pulse_frame, text="📊 The Pulse")
        self.notebook.add(self.autopilot_frame, text="🚀 AutoPilot")
        self.notebook.add(self.rooms_frame, text="🏛️ Rooms")

        self.create_the_pulse_frame()
        self.create_autopilot_frame()
        self.create_rooms_frame()

    def create_the_pulse_frame(self):
        tk.Label(self.the_pulse_frame, text="📌 Task Overview", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
        task_box = tk.Text(self.the_pulse_frame, height=8, width=60, font=("Arial", 12), bg="#f7f7f7", relief="solid")
        task_box.pack(pady=5)

        tk.Label(self.the_pulse_frame, text="📈 Live Feed & Insights", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
        feed_box = tk.Text(self.the_pulse_frame, height=6, width=60, font=("Arial", 12), bg="#f7f7f7", relief="solid")
        feed_box.pack(pady=5)

        btn = tk.Button(self.the_pulse_frame, text="✨ Launch AutoPilot", command=self.autopilot_action,
                        font=("Arial", 12), bg="#0077cc", fg="white", width=20)
        btn.pack(pady=15)

    def create_autopilot_frame(self):
        tk.Label(self.autopilot_frame, text="🎯 Select Focus Mode", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

        self.mode_var = tk.StringVar(value="Do")
        mode_menu = tk.OptionMenu(self.autopilot_frame, self.mode_var, "Do", "Think", "Plan")
        mode_menu.config(font=("Arial", 12))
        mode_menu.pack(pady=5)

        tk.Label(self.autopilot_frame, text="🗂️ Choose Task", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

        self.task_var = tk.StringVar(value="Task 1")
        task_menu = tk.OptionMenu(self.autopilot_frame, self.task_var, "Task 1", "Task 2", "Task 3")
        task_menu.config(font=("Arial", 12))
        task_menu.pack(pady=5)

        start_btn = tk.Button(self.autopilot_frame, text="▶ Start Task", font=("Arial", 12),
                              bg="#28a745", fg="white", width=20, command=self.start_action)
        start_btn.pack(pady=20)

    def create_rooms_frame(self):
        tk.Label(self.rooms_frame, text="🏛️ Your Rooms", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

        self.room_list = tk.Listbox(self.rooms_frame, width=50, height=6, font=("Arial", 12), bg="#f7f7f7", relief="solid")
        for room in ["Strategy Room", "Courtroom AI", "Game Room", "Abeeha’s Room"]:
            self.room_list.insert("end", room)
        self.room_list.pack(pady=10)

        open_btn = tk.Button(self.rooms_frame, text="🗂 Open Selected Room", font=("Arial", 12),
                             bg="#6c63ff", fg="white", width=25, command=self.open_room_action)
        open_btn.pack(pady=15)

    def autopilot_action(self):
        print(f"[AutoPilot] Mode: {self.mode_var.get()} — Suggested action triggered.")

    def start_action(self):
        print(f"[AutoPilot] Starting: {self.task_var.get()}")

    def open_room_action(self):
        selected = self.room_list.curselection()
        if selected:
            room = self.room_list.get(selected)
            print(f"[Room] Opening: {room}")
        else:
            print("[Room] Please select a room.")

if __name__ == "__main__":
    app = SyncMindApp()
    app.mainloop()
