import sqlite3
from PIL import Image
import io

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Retrieve the image data from the database
blog_id = 1  # Replace with the desired row ID
cursor.execute('SELECT image FROM bloggers WHERE id = ?', (blog_id,))
row = cursor.fetchone()

if row is not None and len(row) > 0:
    image_data = row[0]

    # Convert the image data to an image object
    image = Image.open(io.BytesIO(image_data))

    # Display the image
    image.show()
else:
    print(f"No image found for row ID: {blog_id}")

# Close the connection
conn.close()
