#!/usr/bin/python3
"""
A script to connect to a MySQL database and list all states.

Usage: python script.py <username> <password> <database>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
