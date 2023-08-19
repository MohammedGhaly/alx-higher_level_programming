#!/usr/bin/python3
'''
    a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database.
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
    cur.execute("""SELECT c.name
                   FROM cities c
                   JOIN states s
                   ON c.state_id = s.id
                   WHERE s.name = %s
                   ORDER BY c.id ASC""", (sys.argv[4],))

    data = cur.fetchall()
    data_list = []
    for item in data:
        data_list += [item[0]]
    s = ', '.join(data_list)
    print(s)

    cur.close()
    db.close()
