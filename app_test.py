import unittest
import pyperclip
from account import Account
from password import Password
from user import User
from credentials import Credentials

class AppTest(unittest.TestCase):
    '''
    Test class that defines test cases for Password Locker app behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.account_obj=Account("Twitter", "collin", "collin123")
        self.user_obj=User("collin", "collin123")
        self.credentials_obj=Credentials()

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list=[]

    def test_account_init(self):
        '''
        test_account_init method to test if objects of class Account are initialized properly.
        '''
        self.assertEqual(self.account_obj.acc_nm, "Twitter")
        self.assertEqual(self.account_obj.acc_uname, "collin")
        self.assertEqual(self.account_obj.acc_pass, "collin123")

    def test_gen_password(self):
        '''
        test_gen_password method to test if password of inputted length is generated.
        '''
        print(" ")
        print("Generate system password test. Use any inputs.")
        print("-"*40)
        pass_length=int(input("Test sys password length (at least 5): "))
        self.assertEqual(len(Password.gen_password()), pass_length)

    def test_gen_password_copy(self):
        '''
        test_gen_password_copy to test if password generated is copied to clipboard.
        '''
        print(" ")
        print("Copy system password to clipboard test")
        print("-"*40)
        self.assertEqual(Password.gen_password(), pyperclip.paste())  

    def test_user_init(self):
        '''
        test_user_init method to test if objects of class User are initialized properly.
        '''
        self.assertEqual(self.user_obj.username, "collin")
        self.assertEqual(self.user_obj.password, "collin123")

    def test_add_user(self):
        '''
        test_add_user method to test if user can be added to users_list.
        '''
        self.user_obj.add_user(self.user_obj)
        self.assertEqual(len(User.users_list),1)

    def test_add_multiple_users(self):
        '''
        test_add_multiple_users method to test if multiple users can be added to users_list.
        '''
        self.user_obj.add_user(self.user_obj)
        other_user_object=User("John", "doe123")
        other_user_object.add_user(other_user_object)      
        self.assertEqual(len(User.users_list),2)

    def test_check_login(self):
        '''
        test_check_login method to test if true is returned for right login credentials.
        '''
        self.user_obj.add_user(self.user_obj)
        self.assertTrue(self.user_obj.check_login("collin", "collin123"))

    def test_return_user(self):
        '''
        test_return_user method to test if right user object is returned upon login.
        '''
        self.user_obj.add_user(self.user_obj)
        self.assertEqual(User.return_user("collin", "collin123"), self.user_obj)

    def test_add_credential(self):
        '''
        test_add_credential method to test if existing credential can be added to credentials_list.
        '''
        print(" ")
        print("Add credential test")
        print("-"*40)
        self.credentials_obj.add_credential()
        self.assertEqual(len(self.credentials_obj.credentials_list),1)

    def test_create_credential_sys_password(self):
        '''
        test_create_credential_sys_password method to test if new credential can be created with a system generated password.
        '''
        print(" ")
        print("Create credential with system password test")
        print("-"*40)
        self.credentials_obj.create_credential()
        self.assertEqual(len(self.credentials_obj.credentials_list),1) 

    def test_create_credential_custom_password(self):
        '''
        test_create_credential_custom_password method to test if new credential can be created with a custom password.
        '''
        print(" ")
        print("Create credential with custom password test")
        print("-"*40)
        self.credentials_obj.create_credential()
        self.assertEqual(len(self.credentials_obj.credentials_list),1)     

    def test_delete_credential(self):
        '''
        test_delete_credential method to test if credential can be deleted.
        '''
        print(" ")
        print("Delete credential test")
        print("-"*40)
        self.credentials_obj.add_credential()
        self.credentials_obj.delete_credential()   
        self.assertEqual(len(self.credentials_obj.credentials_list),0)

    def test_copy_credential(self):
        '''
        test_copy_credential method to test if credential username and password are copied to clipboard.
        '''
        print(" ")
        print("Copy credential test. Use any account name, username: 'collin', password: 'collin123'")
        print("-"*40)
        self.credentials_obj.add_credential()
        self.credentials_obj.copy_credential()
        self.assertEqual(pyperclip.paste(), "collin collin123")


if __name__=='__main__':
    unittest.main()