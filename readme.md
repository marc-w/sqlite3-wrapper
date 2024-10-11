# SQLite3 Wrapper

Often I need to use SQLite3 but no ORM.  Work such as scrapers need a 
persistent DB, similar to various local scripts.

This library is intended to provide a iminmal wrapper class and referense
for SQLite3 operation.

This work is based on Python's documentation here:

https://docs.python.org/3/library/sqlite3.html

## Example


```
from sqlitehelper import SQLiteHelper, OperationalError

# instantiate class sending in the name of the table
sql = SQLiteHelper(table_name="scrape")

# Create the table, wrap in try/catch to to keep this code in the local script
try:
    sql.cur.execute("CREATE TABLE scrape(url, data)")
except OperationalError:
    pass

# Write data using tuples, single or in list
many = [
    ("url1', "some data 1"),
    ("url2', "some data 2"),
]
sql.write(many)

# SInle write

single = ("url1', "some data 1")
sql.write(one)

# Select

res = sql.query("select * from scrape")

# all fo the SQLite3 commands are available.
print(res.fetchall())  

```
