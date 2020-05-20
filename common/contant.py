#拼接路径
import os
base_dir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
datas_dir=os.path.join(base_dir,'datas')
file_dir=os.path.join(datas_dir,'py.xlsx')
testcases=os.path.join(base_dir,'testcases')
reports_dir=os.path.join(base_dir,'reports')
reports_html_dir=os.path.join(reports_dir,'reports.html')
conf_dir=os.path.join(base_dir,'conf')
global_dir=os.path.join(conf_dir,'global.conf')
test_dir=os.path.join(conf_dir,'test.conf')
test2_dir=os.path.join(conf_dir,'test2.conf')

logs_dir=os.path.join(base_dir,'logs')
