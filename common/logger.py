import logging
from common.config import ReadConfig
from common import contant
import logging.handlers
import os
config=ReadConfig()
def get_logger(logger_name):
    logger=logging.getLogger(logger_name)
    logger.setLevel('INFO') #收集容器设置级别
    #设置输出格式
    fmt="%(name)s-%(levelno)s-%(levelname)s- %(message)s"
    formatter=logging.Formatter(fmt)

    ch=logging.StreamHandler() #创建控制台输出渠道
    level=config.get('log','stream_handle')
    ch.setLevel(level)
    ch.setFormatter(formatter) #控制台输出格式

    filename= os.path.join(contant.logs_dir,'case.logs')
    fh=logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=20*2014*2014, backupCount=10, encoding='utf-8')
    level=config.get('log','file_handle')
    fh.setLevel(level)
    fh.setFormatter(formatter) #控制台输出格式

    logger.addHandler(ch)
    logger.addHandler(fh)