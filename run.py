#!/usr/bin/env python3.6
from password import Password
from user import User
from credentials import Credentials
password_obj=Password()

def sign_up():
    
    username_signup=" "
    password_signup=" " 

    print("\n")
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
            password_signup=password_obj.gen_password()
            print("Signup successful!")
            print("Your password: "+password_signup)
        elif want_sys_password=="n":
            password_signup=input("Password (at least 5 chars): ")
            password_confirm=input("Confirm password: ")
            if len(password_signup)<5:
                want_password_valid=True
                print("Password too short. Try again.")
            elif password_confirm==password_signup:
                print("Sign up successful!")                
                want_password_valid=False
            else:
                print("Passwords did not match. Try again.")
                want_password_valid=True
        else:
            print("Invalid choice. Choose Y/n")
            want_password_valid=True

    new_user=User(username_signup,password_signup)
    new_user.add_user(new_user)
    login()

        

def login():
    is_login=True
    while is_login:
        print("\n")
        print("-----Log in here-----")
        username_login=input("Username: ")
        password_login=input("Password: ")
        login_valid=User.check_login(username_login, password_login)
        if login_valid:
            print("Login successful!")
            is_login=False
            user=User.return_user(username_login, password_login)
            account_menu(username_login, user)
        else:
            print("Login unsuccessful. Try again.")
            is_login=True


def account_menu(this_user_name, this_user_object):
    print("\n")
    print(f'WELCOME TO YOUR ACCOUNT, {this_user_name.upper()}')
    print("What do you want to do?")
    print("1. Add existing credential - press 1")
    print("2. Create new credential   - press 2")
    print("3. View saved credentials  - press 3")
    print("4. Delete saved credential - press 4")
    print("5. Log out                 - press 5")
    print("6. Exit application        - press 6")
    print("\n")
    
    is_selected=True
    while is_selected:
        selected=input("Press option: ")
        if selected=="1":
            is_selected=False
            this_user_object.credential.add_credential()
        elif selected=="2":
            is_selected=False
            this_user_object.credential.create_credential()
        elif selected=="3":
            is_selected=False
            this_user_object.credential.view_credentials()
        elif selected=="4":
            is_selected=False
            this_user_object.credential.delete_credential()
        elif selected=="5":
            is_selected=False
            logout()
        elif selected=="6":
            is_selected=False
            exit_app()
        else:
            print("Invalid option. Try again.")
            is_selected=True
            


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