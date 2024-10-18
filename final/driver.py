import tkinter as tk
from tkinter import messagebox
from database import update_driver_status
import tkinter as tk
from database import setup_database
from pages import StartPage, UserPage, DriverPage, AdminPage

class DriverPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Driver Job Status", font=('Helvetica', 16)).pack(pady=10)

        # Dropdown for driver status
        tk.Label(self, text="Update Job Status").pack()
        self.status_var = tk.StringVar(self)
        self.status_var.set("En Route")
        tk.OptionMenu(self, self.status_var, "En Route", "Goods Collected", "Delivered").pack()

        # Button to update status
        tk.Button(self, text="Update Status", command=self.update_status).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage)).pack(pady=5)

    def update_status(self):
        status = self.status_var.get()
        update_driver_status(status)
        messagebox.showinfo("Status Updated", f"Driver status updated to: {status}")
