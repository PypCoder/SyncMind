import tkinter as tk
import requests
from tkinter import messagebox

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f4f6f9")

        # Title
        tk.Label(
            self, text="📝 Create Your SyncMind Account",
            font=("Helvetica", 20, "bold"),
            bg="#f4f6f9", fg="#2c3e50"
        ).pack(pady=(40, 10))

        tk.Label(
            self, text="Let's get you started!",
            font=("Helvetica", 12),
            bg="#f4f6f9", fg="#7f8c8d"
        ).pack(pady=(0, 20))

        self.username_entry = self.make_input("👤 Username")
        self.email_entry = self.make_input("📧 Email")
        self.password_entry = self.make_input("🔒 Password", show="*")

        # Sign Up Button
        tk.Button(
            self, text="Sign Up",
            font=("Helvetica", 11, "bold"),
            bg="#27ae60", fg="white",
            activebackground="#1e8449",
            width=20,
            command=self.signup_user
        ).pack(pady=10)

        # Back to login
        tk.Button(
            self,
            text="⬅ Already have an account? Login",
            font=("Helvetica", 9), bg="#f4f6f9", fg="#2980b9", bd=0,
            activeforeground="#1f6f99",
            command=lambda: self.controller.show_frame("LoginPage")
        ).pack(pady=(5, 40))

    def make_input(self, label, show=None):
        frame = tk.Frame(self, bg="#f4f6f9")
        frame.pack(pady=5)

        tk.Label(frame, text=label, font=("Helvetica", 10), bg="#f4f6f9", anchor="w").pack(anchor="w")
        entry = tk.Entry(frame, width=30, font=("Helvetica", 10), show=show)
        entry.pack(ipady=4, pady=2)
        return entry

    def signup_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not all([username, email, password]):
            messagebox.showerror("🚫 Error", "Please fill in all fields.")
            return

        try:
            res = requests.post("http://localhost:5000/syncmind/api/auth/signup", json={
                "username": username,
                "email": email,
                "password": password
            })

            data = res.json()

            if res.status_code == 201:
                messagebox.showinfo("✅ Success", "Account created successfully!")
                self.controller.set_user(data)
                self.controller.show_frame("LoginPage")
            else:
                error_msg = data.get("error", "Something went wrong.")
                messagebox.showerror("Signup Failed", f"❌ {error_msg}")

        except Exception as e:
            messagebox.showerror("Network Error", f"⚠️ Couldn't connect to server.\n{str(e)}")