# from MySQLdb import _mysql
import MySQLdb
# import time
"""solution one: MySQLdb._mysql"""
# db = _mysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='user')
# db.insert()
# db.query("select * from T_users where user_name='www';")
#
# result = db.use_result()
# r = result.fetch_row(2)
# print(r)

""" solution two: MySQLdb cursor"""
# sql = "insert into T_users VALUES(1006, 'WWW', 'w', '1880009991', 'Anhui')"
# cur.execute(sql)
# db.commit()
# time.sleep(1)


class Mysql:
    def __init__(self, host, port, user, pwd, db):
        self.db = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db)
        self.cur = self.db.cursor()

    def query_execution(self, sql):
        self.cur.execute(sql)
        re = self.cur.fetchall()
        return re

    def write_execution(self, sql):
        self.cur.execute(sql)
        self.db.commit()

    def close(self):
        self.cur.close()
        self.db.close()




