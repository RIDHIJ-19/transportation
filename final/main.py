import tkinter as tk
from database import setup_database
from user import UserPage
from driver import DriverPage
from admin import AdminPage
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


# Start Page
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to Transport App", font=('Helvetica', 16)).pack(pady=10)

        tk.Button(self, text="User", command=lambda: master.switch_frame(UserPage)).pack(pady=5)
        tk.Button(self, text="Driver", command=lambda: master.switch_frame(DriverPage)).pack(pady=5)
        tk.Button(self, text="Admin", command=lambda: master.switch_frame(AdminPage)).pack(pady=5)


# Main execution
if __name__ == "__main__":
    setup_database()  # Create database and tables if they don't exist
    app = TransportApp()
    app.mainloop()
