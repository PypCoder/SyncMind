import tkinter as tk
from splash import show_splash
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.pulse import PulsePage
from pages.rooms.reception import ReceptionPage

class SyncMindApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SyncMind")
        self.geometry("900x650")
        self.resizable(False, False)
        self.frames = {}

        # App state
        self.user = None
        self.token = None  # JWT or session key
        self.current_room = None

        # Container for pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        for F in (SignupPage, LoginPage, PulsePage, ReceptionPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_user(self, user_data):
        self.user = user_data
        self.show_frame("PulsePage")

    def get_user(self):
        return self.user

    def open_dynamic_room(self, room_info):
        page_name = room_info["page"]
        module_path = f"pages.rooms.{page_name.lower()}"

        # Import the room class dynamically
        import importlib
        room_module = importlib.import_module(module_path)
        RoomClass = getattr(room_module, page_name)

        # Remove old room if exists
        if "DynamicRoom" in self.frames:
            self.frames["DynamicRoom"].destroy()
            del self.frames["DynamicRoom"]

        # Create new room frame
        frame = RoomClass(self.container, self)
        self.frames["DynamicRoom"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("DynamicRoom")

    def logout(self):
        self.user = None
        self.show_frame("LoginPage")


def start_main_app():
    app = SyncMindApp()
    app.mainloop()

if __name__ == "__main__":
    show_splash(start_main_app)
