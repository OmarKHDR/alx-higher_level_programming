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
    query = "SELECT * FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC;"
    num = cr.execute(query)
    row = cr.fetchall()
    for i in range(num):
        print("{}".format(row[i]))
    cr.close()
    db.close()