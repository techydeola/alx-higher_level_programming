#!/usr/bin/python3
"""
    This script lists all cities from a datbase using MySQLdb
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user='{}'.format(sys.argv[1]),
                         passwd='{}'.format(sys.argv[2]),
                         db='{}'.format(sys.argv[3]))

    c = db.cursor()
    c.execute("SELECT c.id, c.name, s.name "
              "FROM cities c "
              "JOIN  states s "
              "ON c.state_id = s.id "
              "ORDER BY c.id ASC")

    rows = c.fetchall()
    for row in rows:
        print(row)
