import unittest

from mysql_db_helper import DbClient


class DbClientTests(unittest.TestCase):

    def test_query_returns_a_result(self):

        db_client = self.create_db_client()
        query_result = db_client.query("select * from students")

        self.assertEqual(query_result.headers[1], "name")
        self.assertEqual(query_result.rows[0][1], "Niels")

    def test_query_csv_returns_a_csv(self):

        db_client = self.create_db_client()
        csv_result = db_client.query_to_csv("select * from students")

        self.assertEqual(csv_result, "id,name\r\n1,Niels\r\n")

    def create_db_client(self):
        host = "localhost"
        database = "students"
        port = 3306
        user = "foo"
        password = "bar"
        db_client = DbClient(host, database, port, user, password)
        return db_client


if __name__ == '__main__':
    unittest.main()
