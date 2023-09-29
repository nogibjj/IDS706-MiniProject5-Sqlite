"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
import mylib.query as q

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Perform CRUD operations on the database...")

print("Querying data...")
q.read()
q.query1()
q.update()
q.query1()  # test update
q.delete()
q.query1()  # test delete

q.query2()

