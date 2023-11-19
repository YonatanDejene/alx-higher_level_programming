#!/usr/bin/python3
"""List all cities from a database"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        user=sys.argv[1],
        # passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    mycur = mydb.cursor()
    mycur.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name = '{}';".format(sys.argv[4]))
    states = mycur.fetchall()

    print(", ".join([state[1] for state in states]))
