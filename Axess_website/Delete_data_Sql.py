import sqlite3

# Connect to the database
conn = sqlite3.connect('Axess.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Delete a row based on the ID
blog_id = 3  # Replace with the desired ID to delete
cursor.execute('DELETE FROM bloggers WHERE id = ?', (blog_id,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
