#!/usr/bin/python3
"""
    may be here
    please
"""
import MySQLdb
import sys
"""
    docs is important
    but idc
"""
if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cr = db.cursor()
    num = cr.execute("SELECT * FROM states ORDER BY id ASC;")
    row = cr.fetchall()
    for i in range(num):
        print("{}".format(row[i]))
    cr.close()
    db.close()
