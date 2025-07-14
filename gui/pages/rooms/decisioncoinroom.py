import tkinter as tk
import random

class DecisionCoinRoom(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#eafaf1")

        tk.Label(self, text="🎲 Decision Coin", font=("Helvetica", 18, "bold"), bg="#eafaf1").pack(pady=20)

        self.result_label = tk.Label(self, text="Flip the coin and decide!", font=("Helvetica", 12), bg="#eafaf1")
        self.result_label.pack(pady=10)

        tk.Button(self, text="🪙 Flip Coin", command=self.flip_coin).pack(pady=10)
        tk.Button(self, text="⬅ Back", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)

        tk.Label(self, text="Made by Ali Hussnain", font=("Helvetica", 8), bg="#eafaf1", fg="gray").pack(side="bottom", pady=5)

    def flip_coin(self):
        self.result_label.config(text=random.choice(["🟡 Heads", "⚫ Tails"]))
