import unittest
from mylib.extract import extract
from mylib.transform_load import load
import mylib.query as q

class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        # This method will run before every test
        print("Setting up for the test")

    def tearDown(self):
        # This method will run after every test
        print("Tearing down after the test")

    def test_extract(self):
        result = extract()
        self.assertIsNotNone(result)  # Assuming that `extract` should return some value

    def test_load(self):
        result = load()
        self.assertEqual(result, "GroceryDB.db")

    def test_read(self):
        result = q.read()
        self.assertIsNone(result)  # Assuming `read` returns None and only prints to console

    def test_query1(self):
        result = q.query1()
        self.assertIsNone(result)  # Assuming `query1` returns None and only prints to console

    def test_update(self):
        q.update()
        # You might want to query the database to check if update was successful

    def test_delete(self):
        q.delete()
        # You might want to query the database to check if the row was actually deleted


    def test_query2(self):
        result = q.query2()
        self.assertIsNone(result)  # Assuming `query2` returns None and only prints to console


if __name__ == '__main__':
    unittest.main()
