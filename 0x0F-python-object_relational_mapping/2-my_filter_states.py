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
    query = "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY states.id".format(
        city_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
