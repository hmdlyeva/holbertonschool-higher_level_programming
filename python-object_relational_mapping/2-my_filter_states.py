#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        c = db.cursor()
        c.execute("SELECT * FROM `states` WHERE `name` = %s ORDER BY id ASC", (state_name,))
        results = c.fetchall()
        for row in results:
            print(row)
        c.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
