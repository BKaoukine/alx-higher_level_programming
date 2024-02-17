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

arguments = sys.argv

# Establish a connection to the MySQL server
db = MySQLdb.connect(host='localhost', user=arguments[1], passwd=arguments[2], db=arguments[3], port=3306)
cur = db.cursor()

# Execute the SQL query
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the results
states = cur.fetchall()

# Print the results in the desired format
for state in states:
    print(state)

# Close the cursor and connection
cur.close()
db.close()
