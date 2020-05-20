import unittest
from testcases.test_register import Register
from common import contant
import HTMLTestRunnerNew

discover=unittest.defaultTestLoader.discover\
    (contant.testcases, pattern='test_*.py', top_level_dir=None)
with open(contant.reports_html_dir,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='加油加油',
                                            description='测试报告',
                                            tester='漫步者1号')
    runner.run( discover)
