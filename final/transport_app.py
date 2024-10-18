# transport_app.py
import tkinter as tk
from database import setup_database
from pages import StartPage, UserPage, DriverPage, AdminPage

class TransportApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transport App")
        self.geometry("400x400")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    setup_database()  # Create database and tables if they don't exist
    app = TransportApp()
    app.mainloop()
