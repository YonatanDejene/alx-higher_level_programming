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
                   WHERE cities.state_id = states.id;")
    cities = mycur.fetchall()

    for city in cities:
        print(city)
