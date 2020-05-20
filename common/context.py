import re
from common.config import ReadConfig
config=ReadConfig()
class Context:
    admin_user=config.get('data','admin_user')
    admin_pwd=config.get('data','admin_pwd')
    loan_member_id=config.get('data','loan_member_id')
    normal_user=config.get('data','normal_user')
    normal_pwd=config.get('data','normal_pwd')
    normal_member_id=config.get('data','normal_member_id')

    def reples(s):
        print(s)
        p='\$\{(.*?)}'
        while re.search(p, s):
            m=re.search(p, s)
            key=m.group(1) #提取
            if hasattr(Context,key):#判断是否存在
                 value=getattr(Context,key) #获取动态属性
                 s=re.sub(p, value, s, count=1)
            else:
                return None
        return s