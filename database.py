import sqlite3
import datetime

# Function to create the database and the raffle_entries table
def create_database():
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS raffle_entries
                 (id INTEGER PRIMARY KEY,
                  shoe TEXT,
                  model TEXT,
                  colourway TEXT,
                  potential_cost REAL,
                  shipping_cost REAL,
                  raffle_drawn DATETIME,
                  store TEXT)''')
    conn.commit()
    conn.close()

# Function to add a raffle entry to the database
def add_raffle_entry(shoe, model, colourway, potential_cost, shipping_cost, raffle_drawn, store):
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    c.execute("INSERT INTO raffle_entries (shoe, model, colourway, potential_cost, shipping_cost, raffle_drawn, store) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (shoe, model, colourway, potential_cost, shipping_cost, raffle_drawn, store))
    conn.commit()
    conn.close()

# Function to remove expired raffles from the database
def remove_expired_raffles():
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    current_time = datetime.datetime.now()
    c.execute("DELETE FROM raffle_entries WHERE raffle_drawn <= ?", (current_time,))
    conn.commit()
    count = c.rowcount  # Get the count of removed entries
    conn.close()
    return count  # Return the count of removed entries
