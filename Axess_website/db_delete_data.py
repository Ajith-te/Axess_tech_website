import sqlite3

conn = sqlite3.connect('Axess.db')
cursor = conn.cursor()

data = [
    ('John', 'Doe', 'john@example.com', '1234567890'),
    ('Jane', 'Smith', 'jane@example.com', '9876543210')
]

cursor.executemany('''INSERT INTO contact (first_name, last_name, email, mobile_number)
                      VALUES (?, ?, ?, ?)''', data)

conn.commit()

conn.close()
