import tkinter as tk

class ReceptionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f4f8")  # Soft background

        # Title
        tk.Label(self, text="🏠 Welcome to the Reception", font=("Helvetica", 20, "bold"),
                 bg="#f0f4f8", fg="#2c3e50").pack(pady=(30, 10))

        # Subtitle
        tk.Label(self, text="🔍 Choose a room to enter:", font=("Helvetica", 12),
                 bg="#f0f4f8", fg="#34495e").pack(pady=(0, 20))

        # Room Buttons
        rooms = [
            {"name": "🧠 Brainstorm Room", "page": "BrainstormRoom"},
            {"name": "⚖️ Courtroom AI", "page": "CourtroomAI"},
            {"name": "📊 EDA Explorer", "page": "EDAExplorer"},
            {"name": "🏡 House Price Predictor", "page": "HousePricePredictor"},
            {"name": "⏳ Focus Timer", "page": "FocusTimer"},
            {"name": "💬 Random Quote", "page": "QuoteRoom"},
            {"name": "🤔 Would You Rather", "page": "WouldYouRatherRoom"},
            {"name": "🎲 Decision Coin", "page": "DecisionCoinRoom"},
        ]

        for room in rooms:
            tk.Button(
                self,
                text=room["name"],
                font=("Helvetica", 11),
                width=32,
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                relief="raised",
                command=lambda r=room: self.controller.open_dynamic_room(r)
            ).pack(pady=6)

        # Back to Pulse
        tk.Button(
            self,
            text="⬅ Back to Pulse",
            font=("Helvetica", 10),
            bg="#dfe6e9",
            command=lambda: controller.show_frame("PulsePage")
        ).pack(pady=(30, 10))
