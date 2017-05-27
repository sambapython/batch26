import unittest
from app import emp
print "sdfsdfsdfsd"

class testcases(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print "calling setup class"
		cls.app_instance = "application instance"
	@classmethod
	def tearDownClass(cls):
		print "teardown class"
		del cls.app_instance
	def setUp(self):
		print self.app_instance
		print "setup"
		print "configure the product for test case"

	def tearDown(self):
		print self.app_instance
		print "teardown"
		print "release the configuration"



	def test_sal_calc_30000_12(self):

		print "running test case1"
		print self.app_instance
		anil = emp('Anil',23,30000,12)
		exp = 33600
		act = anil.sal_calc()
		error = "30000, 12percent exp:%s, got=%s"%(exp,act)
		self.assertEqual(exp,act,error)
		

	def test_sal_calc_30000_None(self):

		print "running test case2"
		print self.app_instance
		anil = emp('Anil',23,30000,None)
		exp = None
		act = anil.sal_calc()
		error = "30000, None exp:%s, got=%s"%(exp,act)
		self.assertEqual(exp,act,error)

	def test_sal_calc_30000_str(self):
		print "running test case3"
		print self.app_instance
		anil = emp('Anil',23,30000,"23")
		exp = None
		act = anil.sal_calc()
		error = "30000, '23' exp:%s, got=%s"%(exp,act)
		self.assertEqual(exp,act,error)
if __name__ == "__main__":
	unittest.main()

