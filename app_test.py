import unittest
import pyperclip
from account import Account

class AppTest(unittest.TestCase):
    def setUp(self):
        self.account_obj=Account("Twitter", "collin", "collin123")

    def tearDown(self):
        pass

    def test_account_init(self):
        self.assertEqual(self.account_obj.acc_nm, "Twitter")
        self.assertEqual(self.account_obj.acc_uname, "collin")
        self.assertEqual(self.account_obj.acc_pass, "collin123")        


if __name__=='__main__':
    unittest.main()