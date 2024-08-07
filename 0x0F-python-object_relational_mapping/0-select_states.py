#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=args[1], passwd=args[2], db = args[3])
    cr = db.cursor()   
    num = cr.execute("SHOW * FROM states ORDER BY states.id")
    row = cr.fetchall()
    for i in range(num):
        print("({}, {}".format(i+1, row[i]))
    cr.close()
    db.close()
