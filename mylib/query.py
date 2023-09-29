"""Query the database"""

import sqlite3
from tabulate import tabulate

def read():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB")
    # print(cursor.fetchall())
    rows = cursor.fetchall()
    rows = rows[-1:-2:-1]
    # Fetching column names
    column_names = [description[0] for description in cursor.description]

    # Use tabulate to format and print the table
    print(tabulate(rows, headers=column_names, tablefmt='grid'))

    conn.close()


def update():
    conn = sqlite3.connect("GroceryDB.db")
    c = conn.cursor()
    c.execute("UPDATE GroceryDB SET general_name = 'Updated Name' WHERE id = 1427")
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("GroceryDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM GroceryDB WHERE id = 1427")
    conn.commit()
    conn.close()


def query1():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB ORDER BY id DESC LIMIT 5")
    print("Bottom 5 rows of the GroceryDB table:")
    rows = cursor.fetchall()

    # If you want them in the original order
    rows = rows[::-1]
    # Fetching column names
    column_names = [description[0] for description in cursor.description]

    # Use tabulate to format and print the table
    print(tabulate(rows, headers=column_names, tablefmt='grid'))

    conn.close()


def query2():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM GroceryDB WHERE avg_FPro_products < 0.5")
    print("The second query ")
    print("Rows with ingredient food processing score < 0.5:")
    rows = cursor.fetchall()

    # Fetching column names
    column_names = [description[0] for description in cursor.description]

    # Use tabulate to format and print the table
    print(tabulate(rows, headers=column_names, tablefmt='grid'))

    conn.close()