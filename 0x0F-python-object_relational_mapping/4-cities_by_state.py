#!/usr/bin/python3
"""
A script to connect to a MySQL database and execute a query.

Usage: python script.py <username> <password> <database>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Main function to connect to the MySQL database and execute a query.
    """
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    # Execute SQL query
    query = "SELECT * FROM cities ORDER BY cities.id"
    cur.execute(query)

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
