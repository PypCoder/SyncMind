import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests

class PulsePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#eef2f7")

        self.rooms_keywords = {
            "Courtroom": ["court", "judge", "verdict"],
            "EDA Room": ["data", "analyze", "eda", "visualize"],
            "Price Predictor": ["price", "house", "prediction"],
            "Focus Timer": ["write", "foucs", "work"],
            "Brainstorm Room": ["ideas", "creativity", "art"],
        }

        # --- Header ---
        tk.Label(
            self,
            text="📊 SyncMind: The Pulse",
            font=("Helvetica", 20, "bold"),
            bg="#eef2f7",
            fg="#2c3e50"
        ).grid(row=0, column=0, columnspan=4, pady=(20, 10))

        # --- Title input ---
        tk.Label(self, text="📌 Title", bg="#eef2f7").grid(row=1, column=0, sticky="w", padx=20)
        self.title_entry = tk.Entry(self, width=50)
        self.title_entry.grid(row=1, column=1, columnspan=3, pady=5, padx=10)

        # --- Description input ---
        tk.Label(self, text="📝 Description", bg="#eef2f7").grid(row=2, column=0, sticky="w", padx=20)
        self.description_input = tk.Text(self, height=3, width=50, font=("Arial", 10))
        self.description_input.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

        # --- Status dropdown ---
        tk.Label(self, text="⚙️ Status", bg="#eef2f7").grid(row=3, column=0, sticky="w", padx=20)
        self.status_var = tk.StringVar(value="pending")
        status_dropdown = ttk.Combobox(
            self,
            textvariable=self.status_var,
            values=["pending", "in_progress", "done"],
            state="readonly",
            width=20
        )
        status_dropdown.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        # --- Due Date input ---
        tk.Label(self, text="📅 Due Date (YYYY-MM-DD)", bg="#eef2f7").grid(row=3, column=2, sticky="e", padx=10)
        self.due_date_entry = tk.Entry(self, width=20)
        self.due_date_entry.grid(row=3, column=3, sticky="w", padx=10, pady=5)

        # --- Add Task Button ---
        tk.Button(
            self,
            text="➕ Add Task",
            font=("Helvetica", 11),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            command=self.create_task
        ).grid(row=4, column=0, columnspan=4, pady=(10, 5), ipadx=10, ipady=2)

        # --- Rooms Button ---
        tk.Button(
            self,
            text="🏠 Go to Rooms",
            font=("Helvetica", 11, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            relief="raised",
            bd=2,
            padx=10,
            pady=5,
            command=lambda: self.controller.show_frame("ReceptionPage")
        ).grid(row=5, column=0, padx=10, pady=(10, 20))

        # --- Logout Button ---
        tk.Button(
            self,
            text="🚪 Logout",
            font=("Helvetica", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            relief="raised",
            bd=2,
            padx=10,
            pady=5,
            command=self.controller.logout
        ).grid(row=5, column=1, padx=10, pady=(10, 20))

        # --- Refresh Button ---
        tk.Button(
            self,
            text="🔄 Refresh Tasks",
            font=("Helvetica", 11, "bold"),
            bg="#2ecc71",
            fg="white",
            activebackground="#27ae60",
            relief="raised",
            bd=2,
            padx=10,
            pady=5,
            command=self.load_tasks
        ).grid(row=5, column=2, padx=10, pady=(10, 20))

        tk.Label(
            self,
            text="🗃️ Task History",
            font=("Helvetica", 12, "bold"),
            bg="#f4f6f9",
            fg="#7f8c8d"
        ).grid(row=6, column=1, columnspan=4, pady=(20, 5), sticky="w")

        # --- Task Table Setup ---
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", font=("Helvetica", 9))

        self.task_table = ttk.Treeview(
            self,
            columns=("Title", "Status", "Suggested Room", "Due Date", "Created At", "Description"),
            show="headings",
            height=12
        )
        for col in self.task_table["columns"]:
            self.task_table.heading(col, text=col)
            self.task_table.column(col, width=120)
        self.task_table.column("Description", width=220)

        self.task_table.grid(row=7, column=0, columnspan=4, padx=20, pady=20)

    def detect_room(self, content):
        content = content.lower()
        for room, keywords in self.rooms_keywords.items():
            for keyword in keywords:
                if keyword in content:
                    return room
        return "General"

    def create_task(self):
        title = self.title_entry.get().strip()
        description = self.description_input.get("1.0", tk.END).strip()
        due_date = self.due_date_entry.get().strip()
        status = self.status_var.get()

        if not title or not description:
            messagebox.showerror("Empty Fields", "⚠️ Title and description cannot be empty.")
            return

        room = self.detect_room(description)
        created_at = datetime.now().isoformat()

        # Compose task payload
        task_payload = {
            "title": title,
            "description": description,
            "status": status,
            "user_id": self.controller.get_user(),
            "due_date": due_date,
            "room": room
        }

        try:
            response = requests.post("http://localhost:5000/syncmind/api/pulse/create_task", json=task_payload)
            response.raise_for_status()  # Raise error if request fails

            if response.status_code == 201:
                data = response.json()

                # Insert into UI table
                self.task_table.insert("", "end", values=(
                    data['title'], data['status'], data['room'],
                    data['due_date'], created_at, data['description']
                ))

                # Clear inputs
                self.title_entry.delete(0, tk.END)
                self.description_input.delete("1.0", tk.END)
                self.due_date_entry.delete(0, tk.END)
                self.status_var.set("pending")

                messagebox.showinfo("✅ Task Added", "Your task has been added and synced with Supabase.")
            else:
                messagebox.showerror("❌ Server Error", f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("❌ Network Error", str(e))


    def load_tasks(self):
        try:
            user_id = self.controller.get_user()

            response = requests.get(
                "http://localhost:5000/syncmind/api/pulse/get_tasks",
                params={"user_id": user_id}
            )

            response.raise_for_status()  # Raise error if request fails
            data = response.json()

            if response.status_code == 201 or response.status_code == 200:
                for task in data:
                    self.task_table.insert("", "end", values=(task['title'], task['status'], 
                    task['room'], task['due_date'], task['created_at'], task['description']))
            else:
                messagebox.showerror("❌ Server Error", f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("❌ Network Error", str(e))
        example_tasks = [
            ("Case Judgment", "in_progress", "Courtroom", "2025-07-14", "Ali", "2025-07-13 09:10", "Judge AI case in court"),
            ("Predict House Price", "pending", "Price Predictor", "2025-07-15", "Sara", "2025-07-13 10:00", "Predict house price from features"),
            ("EDA Client Data", "done", "EDA Room", "2025-07-12", "You", "2025-07-13 10:15", "EDA of client data"),
        ]
