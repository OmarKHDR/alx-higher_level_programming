#!/usr/bin/python3
""" python is so lame

"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cr = db.cursor()
    nm = args[4].strip('\"')
    query = "SELECT * FROM states WHERE name BINARY LIKE %s ORDER BY id ASC;"
    num = cr.execute(query, (nm + '%',))
    row = cr.fetchall()
    for i in range(num):
        print("{}".format(row[i]))
    cr.close()
    db.close()
