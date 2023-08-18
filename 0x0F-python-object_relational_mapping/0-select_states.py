#!/usr/bin/python3
'''a script that lists all states from the database (hbtn_0e_0_usa)'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,
                         host='localhost')
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    db.close()
