import tkinter as tk
from tkinter import messagebox
import requests

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f4f6f9")

        # --- Title ---
        tk.Label(
            self, text="🔐 Welcome to SyncMind",
            font=("Helvetica", 22, "bold"),
            fg="#2c3e50", bg="#f4f6f9"
        ).pack(pady=(40, 10))

        tk.Label(
            self,
            text="Sign in to continue",
            font=("Helvetica", 12),
            fg="#7f8c8d", bg="#f4f6f9"
        ).pack(pady=(0, 20))

        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        form_frame = tk.Frame(self, bg="#f4f6f9")
        form_frame.pack()

        # --- Email Field ---
        tk.Label(form_frame, text="📧 Email", font=("Helvetica", 10), bg="#f4f6f9", anchor="w").grid(row=0, column=0, sticky="w", padx=10)
        email_entry = tk.Entry(form_frame, textvariable=self.email_var, width=30, font=("Helvetica", 10))
        email_entry.grid(row=1, column=0, padx=10, pady=(0, 15), ipady=5)

        # --- Password Field ---
        tk.Label(form_frame, text="🔒 Password", font=("Helvetica", 10), bg="#f4f6f9", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
        password_entry = tk.Entry(form_frame, textvariable=self.password_var, show="*", width=30, font=("Helvetica", 10))
        password_entry.grid(row=3, column=0, padx=10, pady=(0, 20), ipady=5)

        # --- Login Button ---
        login_btn = tk.Button(
            self, text="Login", font=("Helvetica", 11, "bold"),
            bg="#3498db", fg="white", activebackground="#2980b9",
            width=20, command=self.login
        )
        login_btn.pack(pady=5)

        # --- Signup Navigation ---
        tk.Button(
            self, text="Don't have an Account? Signup →",
            font=("Helvetica", 9), bg="#f4f6f9", fg="#2980b9", bd=0,
            activeforeground="#1f6f99",
            command=lambda: self.controller.show_frame("SignupPage")
        ).pack(pady=(10, 40))

    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()

        if not all([email, password]):
            messagebox.showerror("🚫 Error", "Please fill all fields.")
            return

        try:
            response = requests.post("http://localhost:5000/syncmind/api/auth/login", json={
                "email": email,
                "password": password
            })
            if response.status_code == 200:
                data = response.json()
                self.controller.set_user(data["user"])
                self.controller.show_frame("PulsePage")
            else:
                messagebox.showerror("Login Failed", "❌ Incorrect credentials. Please try again.")
        except Exception as e:
            messagebox.showerror("Server Error", f"⚠️ Could not reach server.\n{e}")
