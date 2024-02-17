#!/usr/bin/python3
"""
A script to connect to a MySQL database and execute a query.

Usage: python script.py <username> <password> <database> <query_column>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.
    query_column (str): Name of the column to query from the 'states' table.
"""

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
    user_input = sys.argv[4]

    # Execute SQL query with parameterized query
    query = query = "SELECT * FROM states WHERE name \
    LIKE BINARY %s ORDER BY states.id"

    cur.execute(query, (user_input,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
