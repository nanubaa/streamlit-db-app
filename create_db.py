import sqlite3

# Connect to the database file (it will be created if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named 'users' if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    email TEXT, 
    age INTEGER
)
''')

# Save the changes
conn.commit()

# Close the connection
conn.close()

print("Database and table created successfully.")