import unittest
from ddt import ddt,data
from common.do_excel import DoExcel
from common import contant
from common.request import Requests
from common.context import Context
from common.mysql import MySqlUtil


do_excel=DoExcel(contant.file_dir,'invest')
cases=do_excel.get_data()
request=Requests()



@ddt
class Invest(unittest.TestCase):
    def setUp(self):
        self.mysql = MySqlUtil()
    @data(*cases)
    def test_invest(self,case):
        print('开始执行{}条测试案例'.format(case.case_id))
        case.data=Context.reples(case.data)

        resp=request.request(case.method,case.url,case.data)
        sql ="select id from future.loan WHERE MemberID='343084' ORDER BY CreateTime DESC LIMIT 1"
        loan_id= self.mysql.fetchone(sql)[0]
        setattr(Context,'loan_id',str(loan_id))
        try:
            result = 'PASS'
            import  json
            resp_code=json.loads(resp.text)
            self.assertEqual(case.expected,int(resp_code['code']))
        except AssertionError as e:
            result = 'False'
            print('断言报错了{}'.format(e))
            raise e
        finally:
            do_excel.write_data(case.case_id+1,7,result)
            do_excel.write_data(case.case_id+1,8,result)


if __name__ == '__main__':
    unittest.main()

