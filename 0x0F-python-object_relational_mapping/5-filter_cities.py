#!/usr/bin/python3
import sys
import MySQLdb
"""
lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=db_name)
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name
        FROM cities JOIN states ON states.id = cities.state_id
        WHERE states.name = %(state_name)s
        ORDER BY cities.id""", {'state_name': state_name})

    rows = cursor.fetchall()
    rows = [row[0] for row in rows]
    print(*rows, sep=", ")
