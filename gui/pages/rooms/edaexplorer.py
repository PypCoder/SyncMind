import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import json

class EDAExplorer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="📊 EDA Explorer", font=("Helvetica", 18, "bold")).pack(pady=10)

        tk.Button(self, text="📂 Load CSV File", command=self.load_csv, bg="#3498db", fg="white", font=("Helvetica", 10)).pack(pady=10)

        self.result_text = tk.Text(self, height=25, width=100, font=("Consolas", 9))
        self.result_text.pack()

        tk.Button(self, text="⬅ Back to Reception", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)
        tk.Label(self, text="Made by Muhammad Asad Ullah", font=("Helvetica", 8), bg="#eafaf1", fg="gray").pack(side="bottom", pady=5)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, "rb") as f:
                files = {"file": f}
                response = requests.post("http://localhost:5000/syncmind/api/rooms/explore", files=files)

            if response.status_code != 200:
                raise Exception(response.json().get("error", "Unknown error"))

            data = response.json()
            # Parsing
            shape = data["shape"]
            head = data["head"]
            describe = data["describe"]
            nulls = data["nulls"]
            columns = data.get("columns", [])
            dtypes = data.get("dtypes", {})
            uniques = data.get("unique_values", {})
            memory = data.get("memory_usage_MB", "?")

            # Output formatting
            result = f"✅ File loaded: {file_path}\n\n"
            result += f"🔢 Shape: {shape}\n"
            result += f"🧩 Columns: {columns}\n"
            result += f"📦 Dtypes: {dtypes}\n"
            result += f"🧠 Unique Values: {uniques}\n"
            result += f"💾 Memory Usage: {memory} MB\n\n"

            result += "🧾 Head (First 5 rows):\n"
            for i, row in enumerate(head, 1):
                result += f"  {i}. {row}\n"

            result += "\n📈 Describe:\n"
            for col, stats in describe.items():
                result += f"  ▶ {col}:\n"
                for stat, val in stats.items():
                    result += f"    • {stat}: {val}\n"

            result += "\n❓ Null Values:\n"
            for col, val in nulls.items():
                result += f"  • {col}: {val}\n"

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("❌ Error", str(e))
