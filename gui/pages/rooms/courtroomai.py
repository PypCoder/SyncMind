import tkinter as tk
from tkinter import messagebox
import requests

class CourtroomAI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f9f9fb")

        tk.Label(self, text="⚖️ Courtroom AI", font=("Helvetica", 18, "bold"), bg="#f9f9fb").pack(pady=10)

        tk.Label(self, text="Choose your lawyer side:", font=("Helvetica", 12), bg="#f9f9fb").pack()

        self.choice = tk.StringVar(value="A")
        tk.Radiobutton(self, text="Lawyer A", variable=self.choice, value="A", bg="#f9f9fb").pack()
        tk.Radiobutton(self, text="Lawyer B", variable=self.choice, value="B", bg="#f9f9fb").pack()

        tk.Button(self, text="🎤 Start Debate", command=self.run_debate, bg="#3498db", fg="white").pack(pady=10)

        self.result_text = tk.Text(self, height=20, width=80, wrap="word", font=("Consolas", 10))
        self.result_text.pack(padx=10, pady=10)

        tk.Button(self, text="⬅ Back to Reception", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=10)
        tk.Label(self, text="Made by Muhammad Asad Ullah", font=("Helvetica", 8), bg="#eafaf1", fg="gray").pack(side="bottom", pady=5)

    def run_debate(self):
        self.result_text.delete("1.0", tk.END)
        try:
            response = requests.post("http://localhost:5000/syncmind/api/rooms/debate")
            if response.status_code != 200:
                raise Exception("Invalid response from server.")

            data = response.json()

            self.result_text.insert(tk.END, "📄 Case Summary:\n", "bold")
            self.result_text.insert(tk.END, data["summary"] + "\n\n")

            self.result_text.insert(tk.END, "🗣 Lawyer A:\n", "bold")
            for line in data["lawyer_a"]:
                self.result_text.insert(tk.END, f"• {line}\n")

            self.result_text.insert(tk.END, "\n🗣 Lawyer B:\n", "bold")
            for line in data["lawyer_b"]:
                self.result_text.insert(tk.END, f"• {line}\n")

            self.result_text.insert(tk.END, f"\n👨‍⚖️ Judge's Verdict:\n{data['verdict']}", "verdict")

            self.result_text.tag_config("bold", font=("Consolas", 10, "bold"))
            self.result_text.tag_config("verdict", foreground="darkgreen", font=("Helvetica", 11, "bold"))

        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to fetch debate: {e}")
