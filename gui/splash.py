import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
import threading

def show_splash(main_callback):
    splash = tk.Tk()
    splash.overrideredirect(True)  # No border or buttons
    splash.geometry("400x300+500+250")  # Adjust to center of screen

    splash.configure(bg="#f0f8ff")
    tk.Label(splash, text="🔄 Loading SyncMind...", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=20)
    progress = ttk.Progressbar(splash, mode="indeterminate")
    progress.pack(pady=10)
    progress.start()



    logo = ImageTk.PhotoImage(Image.open("assets/icon_image_3.jpg"))
    tk.Label(splash, image=logo).pack()

    splash.after(2500, lambda: [progress.stop(), splash.destroy(), main_callback()])

    splash.mainloop()
