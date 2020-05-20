import unittest
from ddt import ddt,data
from common.do_excel import DoExcel
from common import contant
from common.request import Requests
from common.mysql import MySqlUtil

do_excel= DoExcel(contant.file_dir,'register')
cases=do_excel.get_data()
requests=Requests()

@ddt
class Register(unittest.TestCase):
    def setUp(self):
        self.sql = "select MAX(mobilephone)FROM future.member WHERE mobilephone LIKE '181%'"
        self.mysql_max = MySqlUtil().fetchone(self.sql)[0]
    @data(*cases)
    def test_register(self,case):
        print("执行第{}条案例".format(case.case_id))
        import json
        case.dict=json.loads(case.data)
        if case.dict['mobilephone']=="${mobilephone}":
            case.dict['mobilephone']=int(self.mysql_max)+1
        resp=requests.request(case.method,case.url,case.dict)

        try:
            result='PASS'
            self.assertEqual(case.expected,resp.text)
        except AssertionError as e:
            result='False'
            print('断言报错了{}'.format(e))
            raise e
        finally:
            do_excel.write_data(case.case_id+1,7,result)
            do_excel.write_data(case.case_id+1,8,result)

if __name__ == '__main__':
    unittest.main()
