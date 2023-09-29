"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/GroceryDB_IgFPro.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)  # ignore the first row which is the header in the csv file
    conn = sqlite3.connect('GroceryDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GroceryDB")
    c.execute("CREATE TABLE GroceryDB ("
              "id INTEGER PRIMARY KEY ,"
              "general_name, "
              "count_products INTEGER, "
              "ingred_FPro FLOAT, "
              "avg_FPro_products FLOAT, "
              "avg_distance_root FLOAT, "
              "ingred_normalization_term FLOAT, "
              "semantic_tree_name, "
              "semantic_tree_node)")
    #insert
    c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    # extra row for testing
    c.execute("INSERT INTO GroceryDB VALUES (1427, 'Test Name', 10, 0.999999, 0.99999, 1.83333, 10.0, '', '')")
    conn.commit()
    conn.close()
    return "GroceryDB.db"
