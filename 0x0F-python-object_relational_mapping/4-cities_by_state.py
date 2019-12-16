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

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=db_name)
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON states.id = cities.state_id
        ORDER BY states.id""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
