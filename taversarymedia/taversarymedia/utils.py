from __future__ import print_function
import time

"""Best library is mysqlclient.... Stick to in in py3.7"""


def query_100k(cur):
    t = time.time()
    for _ in range(100000):
        cur.execute("SELECT 1,2,3,4,5,6")
        res = cur.fetchall()
        assert len(res) == 1
        assert res[0] == (1, 2, 3, 4, 5, 6)
    return time.time() - t


def mysql_connector_python():
    import mysql.connector
    conn = mysql.connector.connect(user='root', password="password", host='localhost')
    print("MySQL Connector/Python:", query_100k(conn.cursor()), "[sec]")


def mysqlclient():
    import MySQLdb
    conn = MySQLdb.connect(user='root', password="password", host='localhost')
    print("mysqlclient:", query_100k(conn.cursor()), "[sec]")


def pymysql():
    import pymysql
    conn = pymysql.connect(user='root', password="password", host='localhost')
    print("PyMySQL:", query_100k(conn.cursor()), "[sec]")


for _ in range(3):  # for PyPy warmup
    mysql_connector_python()
    mysqlclient()
    pymysql()
