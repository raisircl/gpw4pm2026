import sqlite3

conn = sqlite3.connect('dbms_project/payroll.db') # if db does not exist then it will be created

# create a cursor responsible for executing SQL commands
cursor = conn.cursor()

# apply crud operations on the database
# Create, Read, Update, Delete

print("Database created and Successfully Connected to SQLite")

conn.close()
