import tkinter as tk
from tkinter import ttk, messagebox
from database import get_admin_data, clear_all_data  # Ensure you import the clear_all_data function
from pages import StartPage, UserPage, DriverPage
from pages import StartPage, UserPage, DriverPage, AdminPage
class AdminPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Admin Dashboard", font=('Helvetica', 16)).pack(pady=10)

        # Create a Treeview widget
        self.tree = ttk.Treeview(self, columns=("ID", "Pickup", "Dropoff", "Vehicle", "Cost"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Pickup", text="Pickup Location")
        self.tree.heading("Dropoff", text="Drop-off Location")
        self.tree.heading("Vehicle", text="Vehicle Type")
        self.tree.heading("Cost", text="Cost ($)")

        # Set column widths
        self.tree.column("ID", width=50)
        self.tree.column("Pickup", width=150)
        self.tree.column("Dropoff", width=150)
        self.tree.column("Vehicle", width=100)
        self.tree.column("Cost", width=100)

        # Add the Treeview to the GUI
        self.tree.pack(pady=10)

        # Fetch and display booking data
        self.load_data()

        # Button to clear all data
        tk.Button(self, text="Clear All Data", command=self.clear_data).pack(pady=5)

        # Button to go back
        tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage)).pack(pady=5)

    def load_data(self):
        # Get all bookings from the database
        bookings = get_admin_data()

        # Clear any existing data in the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new data into the Treeview
        for booking in bookings:
            self.tree.insert("", "end", values=booking)

        # If no data, add a message
        if not bookings:
            self.tree.insert("", "end", values=("No bookings found", "", "", "", ""))

    def clear_data(self):
        # Confirm clearing data
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all booking data?"):
            clear_all_data()  # Clear data in the database
            messagebox.showinfo("Success", "All booking data has been cleared.")
            self.load_data()  # Reload data to reflect changes
