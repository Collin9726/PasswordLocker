import unittest
import pyperclip
from account import Account
from password import Password

class AppTest(unittest.TestCase):
    def setUp(self):
        self.account_obj=Account("Twitter", "collin", "collin123")

    def tearDown(self):
        pass

    def test_account_init(self):
        self.assertEqual(self.account_obj.acc_nm, "Twitter")
        self.assertEqual(self.account_obj.acc_uname, "collin")
        self.assertEqual(self.account_obj.acc_pass, "collin123")

    def test_gen_password(self):
        pass_length=int(input("Test sys password length: "))
        self.assertEqual(len(Password.gen_password()), pass_length)

    def test_gen_password_copy(self):
        self.assertEqual(Password.gen_password(), pyperclip.paste())        


if __name__=='__main__':
    unittest.main()