import sqlite3

connection = sqlite3.connect('db/database.db')

file = open("db/schema.sql")
connection.executescript(file.read())
file.close()

# Python 'with' syntax
# with open('db/schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()

cur = connection.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (f'Placeholder', f'Hi this is a placeholder post for testing purposes. '))

connection.commit()
connection.close()