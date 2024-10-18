import sqlite3

# Ensure database and tables are set up
def setup_database():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pickup TEXT,
        dropoff TEXT,
        vehicle_type TEXT,
        estimated_cost INTEGER
    );''')

    conn.execute('''CREATE TABLE IF NOT EXISTS driver_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT
    );''')

    conn.commit()
    conn.close()

# Database connection functions
def insert_booking(pickup, dropoff, vehicle_type, estimated_cost):
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO bookings (pickup, dropoff, vehicle_type, estimated_cost) VALUES (?, ?, ?, ?)',
                 (pickup, dropoff, vehicle_type, estimated_cost))
    conn.commit()
    conn.close()

def update_driver_status(status):
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO driver_status (status) VALUES (?)', (status,))
    conn.commit()
    conn.close()

def get_admin_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    conn.close()
    return bookings

def clear_all_data():
    conn = sqlite3.connect('database.db')
    # Delete all records from the bookings table
    conn.execute('DELETE FROM bookings')
    # Delete all records from the driver_status table
    conn.execute('DELETE FROM driver_status')
    conn.commit()
    conn.close()
