import database
import sqlite3

# Create or initialize the database
database.create_database()

# Remove expired raffles when the application starts and get the count of removed entries
removed_count = database.remove_expired_raffles()

# Function to add a raffle entry
def add_raffle_entry():
    shoe = input("Enter shoe name: ")
    model = input("Enter model: ")
    colourway = input("Enter colourway: ")
    
    try:
        potential_cost = float(input("Enter potential cost: "))
        shipping_cost = float(input("Enter shipping cost: "))
    except ValueError:
        print("Invalid input. Cost values must be numeric.")
        return
    
    raffle_drawn = input("Enter raffle drawn date and time (YYYY-MM-DD HH:MM:SS): ")
    store = input("Enter store: ")

    # Call the add_raffle_entry function from the database module
    database.add_raffle_entry(shoe, model, colourway, potential_cost, shipping_cost, raffle_drawn, store)
    print("Raffle entry added successfully.")

# Function to view all raffle entries
def view_all_entries():
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    c.execute("SELECT * FROM raffle_entries")
    entries = c.fetchall()
    conn.close()

    if not entries:
        print("No raffle entries found.")
    else:
        print("\nAll Raffle Entries:")
        for entry in entries:
            print(f"ID: {entry[0]}")
            print(f"Shoe: {entry[1]}")
            print(f"Model: {entry[2]}")
            print(f"Colourway: {entry[3]}")
            print(f"Potential Cost: {entry[4]}")
            print(f"Shipping Cost: {entry[5]}")
            print(f"Raffle Drawn: {entry[6]}")
            print(f"Store: {entry[7]}\n")
            
            # Function to delete a raffle entry by ID
def delete_raffle_entry():
    entry_id = input("Enter the ID of the entry you want to delete: ")
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    c.execute("DELETE FROM raffle_entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print(f"Raffle entry with ID {entry_id} deleted successfully.")

# Define a function to interact with the user and manage raffle entries
def main_menu():
    if removed_count > 0:
        print(f"{removed_count} expired raffle entries removed.")
    else:
        print("No expired raffle entries found.")
    
    while True:
        print("\nRaffle Tracking Application")
        print("1. Add a Raffle Entry")
        print("2. View All Entries")
        print("3. Delete an Entry")  # Add this option
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_raffle_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            delete_raffle_entry()  # Call the function to delete an entry
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
