#!/usr/bin/python3
"""
    This module lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost", port=3306,
                     user="{}".format(sys.argv[1]),
                     passwd="{}".format(sys.argv[2]),
                     db="{}".format(sys.argv[3]))
c = db.cursor()

c.execute("SELECT * FROM states ORDER BY id ASC;")

rows = c.fetchall()
for row in rows:
    print(row)
