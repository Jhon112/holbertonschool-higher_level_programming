#!/usr/bin/python3
import sys
import MySQLdb
"""
lists all states from the database hbtn_0e_0_usa:
"""
if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
