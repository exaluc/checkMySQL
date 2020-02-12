# -*- coding: utf-8 -*-
import pymysql.cursors

class MySQLConn:

    @staticmethod
    def create(host, user, password, db, port):
        return Connection(host, user, password, db, port)

class Connection:

    def __init__(self, host, user, password, db, port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.connect = pymysql.connect

    def test(self):
        '''
        retourne ok si le select 1 functionne.
        '''
        try:
            connection_mysql = self.connect(self.host, self.user, self.password, self.db, self.port, cursorclass=pymysql.cursors.DictCursor, connect_timeout=2)
            with connection_mysql.cursor() as cursor:
                sql = """
                    select 1 as checkin;
                    """
                cursor.execute(sql)
                result = cursor.fetchall()[0]
                if result['checkin']:
                    return('OK')
        except Exception as e:
            return e