import tkinter as tk
import random

class WouldYouRatherRoom(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#fef6f0")

        tk.Label(self, text="🤔 Would You Rather", font=("Helvetica", 18, "bold"), bg="#fef6f0").pack(pady=20)

        self.prompt_label = tk.Label(self, text="What would you choose?", font=("Helvetica", 12), wraplength=400, bg="#fef6f0")
        self.prompt_label.pack(pady=10)

        tk.Button(self, text="🎲 Generate Question", command=self.generate_question).pack(pady=10)
        tk.Button(self, text="⬅ Back", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)

        tk.Label(self, text="Made by Subhan Malik", font=("Helvetica", 8), bg="#fef6f0", fg="gray").pack(side="bottom", pady=5)

    def generate_question(self):
        questions = [
            "Would you rather be invisible or be able to fly?",
            "Would you rather have more time or more money?",
            "Would you rather be feared or loved?",
            "Would you rather only be able to whisper or only be able to shout?",
            "Would you rather never use social media again or never watch another movie?",
        ]
        self.prompt_label.config(text=random.choice(questions))
