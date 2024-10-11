"""SQLite wrapper using STDLIB"""
import sqlite3

OperationalError = sqlite3.OperationalError


class SQLiteHelper:
    """The SQLite helper I have needed for a long while"""

    con = None

    def __init__(self, *args, **kwargs):

        self.db_name = kwargs.get("db_name", "db.sqlite3")
        # self.table_name = kwargs.get("table_name")
        self.con = sqlite3.connect(self.db_name)

    @property
    def cur(self):
        """
        Returns cursor
        """
        if self.con:
            return self.con.cursor()
        return None

    def write(self, vals, table):
        """
        vals: tuple or list of tuples (values to insert, must match table columns)
        """
        # make iterable if not list
        if not isinstance(vals, list):
            vals = [vals]
        values = ''
        for item in vals:
            values += f"{str(item)},"
        query = f"INSERT INTO {table} VALUES {values}"
        # remove trailing ","
        if query.endswith(","):
            query = query[0:-1]

        self.cur.execute("INSERT INTO scrape VALUES ('url1', 'data1'),('url2', 'data2')")
        self.con.commit()

    def query(self, stmt):
        """
        Wrapper for statements
        stmt: string, full statement to run
        """
        return self.cur.execute(stmt)
