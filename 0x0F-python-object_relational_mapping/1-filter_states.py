#!/usr/bin/python3
'''
    a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
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
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
