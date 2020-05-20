import configparser
from common import contant
class ReadConfig:
    def __init__(self):
        self.config=configparser.ConfigParser() # 实例化对象
        self.config.read(contant.global_dir)
        open=self.config.getboolean('swicth','open')
        if open:
            self.config.read(contant.test_dir)
        else:
            self.config.read(contant.test2_dir)
    def get(self,section,option):
        return self.config.get(section,option)

