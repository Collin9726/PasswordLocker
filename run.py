#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
credential=Credentials()

def sign_up():
    print("-----Sign up here-----")
    username_valid=True
    while username_valid:
        username_signup=input("Username: ")
        if len(username_signup)<5:
            username_valid=True
            print("Username too short. Try again.")
        else:
            username_valid=False 
        
    want_password_valid=True
    while want_password_valid:
        want_sys_password=input("Want system generated password? (Y/n): ")
        if want_sys_password=="Y":
            want_password_valid=False
            your_password=credential.gen_password()
            print("Your password: "+your_password)
        elif want_sys_password=="n":
            password_signup=input("Password (at least 5 chars): ")
            password_confirm=input("Confirm password: ")
            if len(password_signup)<5:
                want_password_valid=True
                print("Password too short. Try again.")
            elif password_confirm==password_signup:
                print(username_signup)
                print("Your password: "+password_confirm)
                want_password_valid=False
            else:
                print("Passwords did not match. Try again.")
                want_password_valid=True
        else:
            print("Invalid choice. Choose Y/n")
            want_password_valid=True

        

def login():
    print("-----Log in here-----")
    username_login=input("Username: ")
    password_login=input("Password: ")
    print(username_login)
    print(password_login)

def main():
    print("PASSWORD LOCKER")
    print("="*15)
    has_account_valid=True    
    while has_account_valid:
        has_account=input("Have an account? (Y/n): ")
        if has_account=="Y":
            has_account_valid=False
            login()
        elif has_account=="n":
            has_account_valid=False
            sign_up()
        else:
            print("Invalid choice. Choose Y/n")
            has_account_valid=True
    


if __name__ == "__main__":
    main ()