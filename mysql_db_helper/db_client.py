import csv
import io

from MySQLdb import connect

from mysql_db_helper.db_query_result import DbQueryResult


class DbClient:
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password

    def query(self, query) -> DbQueryResult:
        db = connect(host=self.host,
                     user=self.user,
                     passwd=self.password,
                     db=self.database,
                     port=int(self.port)
                     )
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [col[0] for col in cursor.description]
        return DbQueryResult(rows, headers)

    def query_to_csv(self, query) -> str:
        query_result = self.query(query)
        s_buf = io.StringIO()
        csv_writer = csv.writer(s_buf)
        csv_writer.writerow(tuple(query_result.headers))
        csv_writer.writerows(query_result.rows)
        return s_buf.getvalue()
