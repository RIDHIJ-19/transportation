import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy import distance
from database import insert_booking
from tkinter import messagebox
from database import update_driver_status
import tkinter as tk
from database import setup_database
from pages import StartPage, UserPage, DriverPage, AdminPage

# User Page (for booking service)
class UserPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="User Booking Page", font=('Helvetica', 16)).pack(pady=10)

        # Define the pickup and drop-off locations (areas in Delhi)
        self.locations = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
            "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
            "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ]

        # Define the vehicle types
        self.vehicle_types = ["Car", "Truck", "Tempo"]

        # Dropdown for pickup location
        tk.Label(self, text="Pickup Location").pack()
        self.pickup_var = tk.StringVar(value=self.locations[0])  # Default value
        self.pickup_menu = tk.OptionMenu(self, self.pickup_var, *self.locations)
        self.pickup_menu.pack()

        # Dropdown for drop-off location
        tk.Label(self, text="Drop-off Location").pack()
        self.dropoff_var = tk.StringVar(value=self.locations[0])  # Default value
        self.dropoff_menu = tk.OptionMenu(self, self.dropoff_var, *self.locations)
        self.dropoff_menu.pack()

        # Dropdown for vehicle type
        tk.Label(self, text="Vehicle Type").pack()
        self.vehicle_type_var = tk.StringVar(value=self.vehicle_types[0])  # Default value
        self.vehicle_menu = tk.OptionMenu(self, self.vehicle_type_var, *self.vehicle_types)
        self.vehicle_menu.pack()

        # Button to book
        tk.Button(self, text="Book", command=self.book_vehicle).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage)).pack(pady=5)

    def book_vehicle(self):
        # Store selected options in variables
        start = self.pickup_var.get()  # Selected pickup location
        stop = self.dropoff_var.get()  # Selected drop-off location
        mode = self.vehicle_type_var.get()  # Selected vehicle type

        # Calculate distance and estimated cost
        try:
            distance_km, estimated_cost = self.calculate_distance_and_cost(start, stop, mode)
            insert_booking(start, stop, mode, estimated_cost)
            messagebox.showinfo("Booking",
                                f"Vehicle booked from {start} to {stop}.\n"
                                f"Vehicle Type: {mode}\n"
                                f"Estimated Distance: {distance_km:.2f} km\n"
                                f"Estimated Cost: ${estimated_cost:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate_distance_and_cost(self, start, stop, mode):
        # Initialize the geocoder
        geolocator = Nominatim(user_agent="Your Application Name")

        # Get the coordinates for the pickup and drop-off locations
        pickup_location = f"{start}, India"
        dropoff_location = f"{stop}, India"
        pickup_coords = geolocator.geocode(pickup_location)
        dropoff_coords = geolocator.geocode(dropoff_location)

        if pickup_coords is None or dropoff_coords is None:
            raise ValueError("Invalid pickup or drop-off location.")

        # Extract latitude and longitude from the coordinates
        lat1, lon1 = pickup_coords.latitude, pickup_coords.longitude
        lat2, lon2 = dropoff_coords.latitude, dropoff_coords.longitude

        # Calculate the distance in kilometers
        distance_km = distance.distance((lat1, lon1), (lat2, lon2)).km

        # Calculate cost based on vehicle type
        cost_per_km = 0
        if mode == "Car":
            cost_per_km = 10
        elif mode == "Truck":
            cost_per_km = 30
        elif mode == "Tempo":
            cost_per_km = 45

        # Calculate the total estimated cost
        estimated_cost = distance_km * cost_per_km
        return distance_km, estimated_cost


# Main application
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Vehicle Booking System")
        self.geometry("400x400")
        self.frames = {}
        self.switch_frame(UserPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if new_frame not in self.frames.values():
            self.frames[frame_class] = new_frame
            new_frame.pack(fill='both', expand=True)
        for frame in self.frames.values():
            if frame != new_frame:
                frame.pack_forget()


if __name__ == "__main__":
    app = App()
    app.mainloop()
