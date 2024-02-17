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
    arguments = sys.argv

    db = MySQLdb.connect(host='localhost', user=arguments[1], passwd=arguments[2], db=arguments[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
