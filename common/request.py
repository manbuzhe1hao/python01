import requests
import json
from common.mysql import MySqlUtil
from common.config import ReadConfig
mysql=MySqlUtil()
config=ReadConfig()
class Requests:
    def __init__(self):
        self.sission=requests.session()
    def request(self,method,url,data):
        method=method.upper()
        pre_url=config.get('api','pre_url')
        url=pre_url+url #拼接
        print(url)
        if data is not None and type(data)==str:
            data=json.loads(data) #将字符串转换成字典
        if method=='GET':
            return self.sission.request(method,url,params=data)
        elif method=='POST':
            return self.sission.request(method,url,data=data)
        else:
            print('请求方式填写错误！！')


