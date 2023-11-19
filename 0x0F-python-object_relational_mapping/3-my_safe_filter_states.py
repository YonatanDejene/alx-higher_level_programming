#!/usr/bin/python3
"""Lists all values in the states tables of a database where name
matches the argument in a safe way"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = mycur.fetchall()

    for state in states:
        print(state)
