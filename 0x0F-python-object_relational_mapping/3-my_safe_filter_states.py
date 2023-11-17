#!/usr/bin/python3
"""
    This module lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user="{}".format(sys.argv[1]),
                         passwd="{}".format(sys.argv[2]),
                         db="{}".format(sys.argv[3]))
    c = db.cursor()

    query = """SELECT * FROM states
                WHERE name='%s'
                ORDER BY id ASC """
    c.execute(query, (sys.argv[4]),)

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
