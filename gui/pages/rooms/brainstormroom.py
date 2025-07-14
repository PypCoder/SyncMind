import tkinter as tk
import random

class BrainstormRoom(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f4f6f9")

        tk.Label(self, text="🤖 AI-Powered Brainstorm Room", font=("Helvetica", 20, "bold"),
                 bg="#f4f6f9", fg="#2c3e50").pack(pady=(20, 10))

        self.idea_label = tk.Label(self, text="✨ Click below to get a fresh AI-generated idea!",
                                   font=("Helvetica", 14), bg="#f4f6f9", wraplength=600,
                                   justify="center", fg="#34495e")
        self.idea_label.pack(pady=(10, 20))

        tk.Button(self, text="💡 Generate Smart Idea", font=("Helvetica", 12, "bold"),
                  bg="#3498db", fg="white", activebackground="#2980b9",
                  command=self.generate_ai_idea).pack(pady=10, ipadx=10, ipady=4)

        self.history_title = tk.Label(self, text="🗃️ Idea History", font=("Helvetica", 12, "bold"),
                                      bg="#f4f6f9", fg="#7f8c8d")
        self.history_title.pack(pady=(20, 5))

        self.history_box = tk.Text(self, height=10, width=80, wrap=tk.WORD,
                                   bg="#ecf0f1", fg="#2c3e50")
        self.history_box.pack(padx=20)

        tk.Button(self, text="⬅ Back to Reception", font=("Helvetica", 10),
                  bg="#ecf0f1", command=lambda: controller.show_frame("ReceptionPage")).pack(pady=20)
        tk.Label(self, text="Made by Muhammad Asad Ullah", font=("Helvetica", 8), bg="#eafaf1", fg="gray").pack(side="bottom", pady=5)

    def generate_ai_idea(self):
        # -- AI-style templates with placeholders --
        templates = [
            "Build a {} that helps {} using {}.",
            "Create a platform for {} to {} via {}.",
            "What if we made an AI that could {} using {}?",
            "Design a system to {} for {} using {}.",
            "A smart assistant that {} and {} with {}."
        ]

        problems = [
            "students", "remote teams", "freelancers", "busy parents",
            "mental health coaches", "creators", "developers", "startup founders"
        ]

        goals = [
            "manage tasks", "boost productivity", "track emotions", "generate reports",
            "collaborate better", "organize goals", "track habits", "predict outcomes"
        ]

        tech = [
            "AI", "NLP", "voice recognition", "machine learning", "chatbot interfaces",
            "AR overlays", "data visualizations", "gamified UX", "blockchain"
        ]

        actions = [
            "automate decision making", "transcribe meetings", "suggest improvements",
            "forecast outcomes", "summarize daily logs", "visualize progress",
            "learn from user input", "track productivity trends"
        ]

        # Pick a random template and fill it smartly
        template = random.choice(templates)

        if "{}" in template and template.count("{}") == 3:
            filled = template.format(
                random.choice(goals),
                random.choice(problems),
                random.choice(tech)
            )
        elif "{}" in template and template.count("{}") == 2:
            filled = template.format(
                random.choice(actions),
                random.choice(tech)
            )
        elif template.count("{}") == 1:
            filled = template.format(random.choice(goals))
        else:
            filled = template.format(
                random.choice(actions),
                random.choice(actions),
                random.choice(tech)
            )

        self.idea_label.config(text=filled)
        self.history_box.insert(tk.END, f"• {filled}\n")
        self.history_box.see(tk.END)
