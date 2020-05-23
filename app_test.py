import unittest
import pyperclip
from account import Account
from password import Password
from user import User

class AppTest(unittest.TestCase):
    def setUp(self):
        self.account_obj=Account("Twitter", "collin", "collin123")
        self.user_obj=User("collin", "collin123")

    def tearDown(self):
        User.users_list=[]

    # def test_account_init(self):
    #     self.assertEqual(self.account_obj.acc_nm, "Twitter")
    #     self.assertEqual(self.account_obj.acc_uname, "collin")
    #     self.assertEqual(self.account_obj.acc_pass, "collin123")

    # def test_gen_password(self):
    #     pass_length=int(input("Test sys password length: "))
    #     self.assertEqual(len(Password.gen_password()), pass_length)

    # def test_gen_password_copy(self):
    #     self.assertEqual(Password.gen_password(), pyperclip.paste())  

    def test_user_init(self):
        self.assertEqual(self.user_obj.username, "collin")
        self.assertEqual(self.user_obj.password, "collin123")

    def test_add_user(self):
        self.user_obj.add_user(self.user_obj)
        self.assertEqual(len(User.users_list),1)

    def test_add_multiple_users(self):
        self.user_obj.add_user(self.user_obj)
        other_user_object=User("John", "doe123")
        other_user_object.add_user(other_user_object)      
        self.assertEqual(len(User.users_list),2)

    def test_check_login(self):
        self.user_obj.add_user(self.user_obj)
        self.assertTrue(self.user_obj.check_login("collin", "collin123"))

    def test_return_user(self):
        self.user_obj.add_user(self.user_obj)
        self.assertEqual(User.return_user("collin", "collin123"), self.user_obj)


if __name__=='__main__':
    unittest.main()