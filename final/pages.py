# pages.py
import tkinter as tk
from tkinter import messagebox
from database import insert_booking, get_admin_data, update_driver_status

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to Transport App", font=('Helvetica', 16)).pack(pady=10)

        tk.Button(self, text="User", command=lambda: master.switch_frame(UserPage)).pack(pady=5)
        tk.Button(self, text="Driver", command=lambda: master.switch_frame(DriverPage)).pack(pady=5)
        tk.Button(self, text="Admin", command=lambda: master.switch_frame(AdminPage)).pack(pady=5)

class UserPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="User Booking Page", font=('Helvetica', 16)).pack(pady=10)

        # Input fields
        tk.Label(self, text="Pickup Location").pack()
        self.pickup_entry = tk.Entry(self)
        self.pickup_entry.pack()

        tk.Label(self, text="Drop-off Location").pack()
        self.dropoff_entry = tk.Entry(self)
        self.dropoff_entry.pack()

        tk.Label(self, text="Vehicle Type").pack()
        self.vehicle_type_entry = tk.Entry(self)
        self.vehicle_type_entry.pack()

        # Button to book
        tk.Button(self, text="Book", command=self.book_vehicle).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage)).pack(pady=5)

    def book_vehicle(self):
        pickup = self.pickup_entry.get()
        dropoff = self.dropoff_entry.get()
        vehicle_type = self.vehicle_type_entry.get()
        estimated_cost = 100  # Placeholder logic for estimated cost

        insert_booking(pickup, dropoff, vehicle_type, estimated_cost)
        messagebox.showinfo("Booking", f"Vehicle booked from {pickup} to {dropoff}.\nEstimated cost: ${estimated_cost}")

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

class AdminPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Admin Dashboard", font=('Helvetica', 16)).pack(pady=10)

        # Display booking data
        tk.Label(self, text="All Bookings").pack()
        bookings = get_admin_data()
        for booking in bookings:
            tk.Label(self,
                     text=f"Booking {booking[0]}: {booking[1]} -> {booking[2]}, Vehicle: {booking[3]}, Cost: ${booking[4]}").pack()

        tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage)).pack(pady=5)
