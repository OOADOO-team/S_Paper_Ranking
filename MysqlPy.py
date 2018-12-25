# MysqlPython.py
# 首先导入pymysql，我们目前只用连接的方法
from pymysql import connect


# 创建类
class MysqlHelp(object):
    # 初始化方法
    def __init__(self, database, host='localhost', user='root', password='123456', charset='utf8', port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    # 初始化完后连接到数据库并创建好游标
    def open(self):
        # 连接数据库
        self.conn = connect(host=self.host, user=self.user, password=self.password, database=self.database,
                            charset=self.charset, port=self.port)
        # 创建游标
        self.cur = self.conn.cursor()

    # 有连接数据库，就得有关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()

    # 增删改
    def sql_execute(self, sql, L=[]):
        # 操作就得打开数据库吧
        self.open()
        # 对sql语句处理（即开始操作数据库了）,有成功有失败
        try:
            self.cur.execute(sql, L)  # 执行sql命令
            self.conn.commit()  # 提交到数据库执行
            print('ok')
        except Exception as e:
            self.conn.rollback()
            print('failed', e)
        # 打开数据库就得关闭吧
        self.close()

    # 查
    def getAll(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        # 查询结果用result绑定
        result = self.cur.fetchAll()
        self.close()
        # 将查询到的结果返回回去
        return result


def search(name):
    mysql = MysqlHelp('db4')
    # 要执行的sql语句
    sql_select = 'select * from sys;'
    # 去调用MysqlPython工具里的查询方法
    result = mysql.getAll(sql_select)  # 返回一个元组
    # 打印结果
    for i in result:
        print(i)


def remove(name):
    from MysqlPython import MysqlHelp
    mysql = MysqlHelp('db4')
    sql_delete = 'delete from sheng where s_name=%s'
    mysql.workOn(sql_delete, ['湖北'])


def insert(paper):
    from MysqlPython import MysqlHelp
    mysql = MysqlHelp('db4')
    sql_insert = 'insert into sheng(s_id, s_name) values(%s, %s);'
    mysql.workOn(sql_insert, ['500001', '北京市'])