import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests

class HousePricePredictor(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f4f6f8")
        self.controller = controller

        self.inputs = [
            'area',
            'bedrooms',
            'bathrooms',
            'stories',
            'mainroad',
            'guestroom',
            'basement',
            'hotwaterheating',
            'airconditioning',
            'parking',
            'prefarea',
            'furnishingstatus'
        ]

        field_labels = [
            'Area (m²)',
            'Bedrooms',
            'Bathrooms',
            'Stories',
            'Mainroad (0/1)',
            'Guestroom (0/1)',
            'Basement (0/1)',
            'Hot-water Heating (0/1)',
            'Air Conditioning (0/1)',
            'Parking (0/1)',
            'Prefarea (0/1)',
            'Furnishing Status (0/1/2)'
        ]

        # Title
        tk.Label(
            self,
            text="🏡 House Price Predictor",
            font=("Helvetica", 20, "bold"),
            bg="#f4f6f8",
            fg="#2c3e50"
        ).grid(row=0, column=2, columnspan=2, pady=(20, 10))

        self.entries = {}

        # Input fields in 2-column layout
        for i, label in enumerate(field_labels):
            tk.Label(
                self,
                text=label,
                font=("Helvetica", 10),
                bg="#f4f6f8",
                anchor="w"
            ).grid(row=i + 1, column=2, padx=(20, 5), pady=5, sticky="w")

            entry = tk.Entry(self, width=30)
            entry.grid(row=i + 1, column=3, padx=(0, 20), pady=5)
            self.entries[self.inputs[i]] = entry

        # Predict Button
        tk.Button(
            self,
            text="🔍 Predict Price",
            command=self.start_prediction_thread,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            font=("Helvetica", 11),
            width=20
        ).grid(row=len(field_labels) + 1, column=2, columnspan=2, pady=(20, 5))

        # Result label
        self.result = tk.Label(
            self,
            text="💬 Result will appear here.",
            font=("Helvetica", 12, "italic"),
            bg="#f4f6f8",
            fg="#2c3e50",
            wraplength=400,
            justify="center"
        )
        self.result.grid(row=len(field_labels) + 2, column=2, columnspan=2, pady=(10, 20))

        # Back button
        tk.Button(
            self,
            text="⬅ Back to Reception",
            command=lambda: controller.show_frame("ReceptionPage"),
            bg="#ecf0f1",
            font=("Helvetica", 10)
        ).grid(row=len(field_labels) + 3, column=2, columnspan=2, pady=(5, 20))
        tk.Label(
            self,
            text="Made by Muhammad Asad Ullah",
            font=("Helvetica", 8),
            bg="#eafaf1",
            fg="gray"
        ).grid(row=len(field_labels) + 4, column=2, columnspan=3, pady=5, sticky="s")


    def start_prediction_thread(self):
        threading.Thread(target=self.predict_price, daemon=True).start()

    def predict_price(self):
        self.result.config(text="🔄 Predicting...")
        try:
            # Collect input
            input_data = {}
            for key in self.inputs:
                val = self.entries[key].get()
                if val.strip() == '':
                    messagebox.showerror("⚠️ Missing Data", f"Please fill in: {key}")
                    self.result.config(text="⚠️ Please complete all fields.")
                    return
                input_data[key] = float(val)

            # Send request to backend
            response = requests.post(
                "http://localhost:5000/syncmind/api/rooms/model/predicthouseprice",
                json=input_data
            )

            if response.status_code == 200:
                data = response.json()
                price = data['predicted_price']
                formatted_price = f"${price:,.2f}"
                messagebox.showinfo("✅ Prediction Successful", f"Estimated Price: {formatted_price}")
                self.result.config(text=f"💰 Estimated Price: {formatted_price}")
            else:
                messagebox.showerror("❌ Server Error", "Prediction failed. Please try again.")
                self.result.config(text="❌ Prediction failed. Server error.")

        except Exception as e:
            messagebox.showerror("❌ Error", str(e))
            self.result.config(text=f"❌ Error: {str(e)}")