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
    
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'\
                 ORDER BY states.id".format(sys.argv[4]))
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
