'''

'''

import pymysql


# 装饰器函数
def decorator(fun):
    def func(self, *args, **kwargs):
        try:
            fun(self, *args, **kwargs)
            self._db.commit()
        except Exception as e:
            print("error: ", e)
            return False
        return True
    return func


class Mysql:
    def __init__(self, host, port, user, passwd, db):
        self._create_db(host, port, user, passwd, db)

    def _create_db(self, host, port, user, passwd, db):
        self._db = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=passwd,
                                   database=db,
                                   charset='utf8')
        self._cursor = self._db.cursor()

    def close(self):
        self._cursor.close()
        self._db.close()

    # 单条查询
    def select(self, sql):
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    # 插入，单条
    @decorator
    def insert_one(self, sql):
        self._cursor.execute(sql)

    # 插入, 多条
    @decorator
    def insert_multi(self, sql, data: list):
        self._cursor.executemany(sql, data)

    # 更新数据
    @decorator
    def update(self, sql):
        self._cursor.execute(sql)

    # 删除数据
    @decorator
    def delete(self, sql):
        self._cursor.execute(sql)



if __name__ == '__main__':
    
    pass
