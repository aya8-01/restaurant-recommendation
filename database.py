import sqlite3

conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal TEXT,
    name TEXT
)
""")

data = [
    ("pizza", "Pizza Hut"),
    ("burger", "Burger King"),
    ("shawarma", "Local Shawarma"),
    ("pasta", "Italiano"),
]

cursor.executemany("INSERT INTO restaurants (meal, name) VALUES (?, ?)", data)

conn.commit()
conn.close()

print("Database created successfully")
