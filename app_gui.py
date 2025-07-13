import tkinter as tk
from tkinter import ttk, messagebox
import requests

class SyncMindApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧠 SyncMind with API")
        self.geometry("600x400")

        # AutoPilot Frame only (for demo)
        self.mode_var = tk.StringVar(value="Do")

        ttk.Label(self, text="Select Mode").pack(pady=10)
        ttk.OptionMenu(self, self.mode_var, "Do", "Do", "Think", "Plan").pack()

        tk.Button(self, text="🎯 AutoPilot Suggestion", command=self.get_suggestion,
                  bg="#0077cc", fg="white", font=("Arial", 12)).pack(pady=20)

    def get_suggestion(self):
        mode = self.mode_var.get()
        try:
            res = requests.get(f"http://127.0.0.1:5000/suggest?mode={mode}")
            data = res.json()
            if "title" in data:
                messagebox.showinfo("Suggested Task", f"{data['title']}\n\n{data['description']}")
            else:
                messagebox.showinfo("Info", data.get("message", "No suggestion"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch: {e}")

if __name__ == "__main__":
    app = SyncMindApp()
    app.mainloop()
