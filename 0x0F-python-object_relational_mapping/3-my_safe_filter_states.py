#!/usr/bin/python3
import sys
import MySQLdb
"""
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    city_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=db_name)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name =
            %(city_name)s ORDER BY states.id""", {'city_name': city_name})

    rows = cursor.fetchall()
    for row in rows:
        print(row)
