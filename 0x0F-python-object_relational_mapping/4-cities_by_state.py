#!/usr/bin/python3
'''
    a script that lists all cities from the database hbtn_0e_4_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name AS state
                   FROM cities c
                   JOIN states s
                   ON s.id = c.state_id""")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
