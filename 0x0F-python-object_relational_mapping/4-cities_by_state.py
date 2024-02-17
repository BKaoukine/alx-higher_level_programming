#!/usr/bin/python3


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Main function to connect to the MySQL database and execute a query.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    # Execute SQL query with parameterized query
    query = "SELECT * FROM cities WHERE name ORDER BY cities.id"

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
