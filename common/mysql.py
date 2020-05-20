import pymysql

class MySqlUtil:
    def __init__(self):
        self.host ='test.lemonban.com'
        self.user = 'test'
        self.password = 'test'
        self.mysql=pymysql.connect(host=self.host, user=self.user, password=self.password, port=3306) #连接数据库
        self.crusor=self.mysql.cursor() #打开查询窗口
    def fetchone(self,sql):
        self.crusor.execute(sql) #执行语句
        retult=self.crusor.fetchone() #得到一条查询结果
        return retult
    def close(self):
        self.crusor.close()
        self.mysql.close()

