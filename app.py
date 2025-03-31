import sqlite3

# Connect to SQLite (or create it if it doesn't exist)
conn = sqlite3.connect("hello_world.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
)
''')

# Insert a "Hello, World!" message
cursor.execute("INSERT INTO messages (text) VALUES (?)", ("Hello, World!",))
conn.commit()

# Retrieve and print the message
cursor.execute("SELECT text FROM messages ORDER BY id DESC LIMIT 1")
message = cursor.fetchone()[0]
print(message)

# Close the connection
conn.close()
