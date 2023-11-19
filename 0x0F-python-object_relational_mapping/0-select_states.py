#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

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

    mycur.execute("SELECT * FROM states;")
    states = mycur.fetchall()

    for state in states:
        print(state)
