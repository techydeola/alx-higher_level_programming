#!/usr/bin/python3
"""
    this script takes in the name of a state as an argument and lists
    all cities of that state, using the datbase hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                       user='{}'.format(sys.argv[1]),
                       passwd='{}'.format(sys.argv[2]),
                       db='{}'.format(sys.argv[3]))

    c = db.cursor()
    state_name = sys.argv[4]
    c.execute("SELECT c.name "
              "FROM cities c "
              "JOIN states s "
              "ON c.state_id = s.id "
              "WHERE s.name LIKE %s ", (state_name, ))

    rows = c.fetchall()
    all_items = [item for row in rows for item in row]
    row_str = ', '.join(map(str, all_items))
    print(row_str)
