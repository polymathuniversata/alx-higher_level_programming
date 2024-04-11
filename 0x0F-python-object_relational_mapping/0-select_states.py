#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa using MySQLdb
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Ensure user, passwd, and db are provided as command line arguments
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Execute the query to select all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the results
        states = cur.fetchall()

        # Print states
        for state in states:
            print(state)

        # Close all cursors
        cur.close()
        # Close all databases
        db.close()
    else:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
