#!/usr/bin/python3
'''Get All States, requires User, Password, Database'''
import MySQLdb
import sys


def my_filter_states():
    '''Get States from sql table'''
    if(len(sys.argv) < 5):
        return
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    try:
        db = MySQLdb.connect(
            "localhost",
            mysql_username,
            mysql_password,
            database_name)
    except Exception as e:
        return (0)
    target = sys.argv[4]
    target = target.split('"')[0]
    target = target.split("'")[0]
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states \
        WHERE name LIKE '{}' ORDER BY id ASC;".format(target))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()


if __name__ == '__main__':
    my_filter_states()
