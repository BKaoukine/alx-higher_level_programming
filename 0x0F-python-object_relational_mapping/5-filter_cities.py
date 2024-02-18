#!/usr/bin/python3
"""
A script to connect to a MySQL database and execute a query.

Usage: python script.py <username> <password> <database> <State>

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username>\
               <password> <database> <State>")
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
    stat_name = sys.argv[4]
    # Execute SQL query
    query = "SELECT DISTINCT c.name AS city_name\
            FROM cities AS c\
            JOIN states AS s ON c.state_id = s.id\
            WHERE s.name = %s"

    cur.execute(query, (stat_name,))

    # Fetch and print results
    rows = cur.fetchall()
    print(rows)

    # Close cursor and database connection
    cur.close()
    db.close()
