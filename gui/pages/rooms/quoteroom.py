import tkinter as tk
import random

class QuoteRoom(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f4f8")

        tk.Label(self, text="💬 Random Quote", font=("Helvetica", 18, "bold"), bg="#f0f4f8").pack(pady=20)

        self.quote_label = tk.Label(self, text="Click the button to get inspired!", font=("Helvetica", 12), wraplength=400, bg="#f0f4f8")
        self.quote_label.pack(pady=10)

        tk.Button(self, text="🔁 New Quote", command=self.show_quote).pack(pady=10)

        tk.Button(self, text="⬅ Back", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)

        tk.Label(self, text="Made by Abeeha Ali", font=("Helvetica", 8), bg="#f0f4f8", fg="gray").pack(side="bottom", pady=5)

    def show_quote(self):
        quotes = [
            "The best way to get started is to quit talking and begin doing.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Don’t let yesterday take up too much of today.",
            "You don’t have to be great to start, but you have to start to be great.",
            "Do what you can with all you have, wherever you are.",
        ]
        self.quote_label.config(text=random.choice(quotes))
