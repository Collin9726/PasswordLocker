import password
import account
password_obj1=password.Password()
class Credentials:
    credentials_list=[]
    
    def add_credential(self):
        print(" ")
        print("-----Add credential here-----")
        acc_name=input("Account name: ")
        acc_username=input("Account username: ")
        acc_password=input("Account password: ")
        new_account=account.Account(acc_name,acc_username,acc_password)
        self.credentials_list.append(new_account)
        print(f'{acc_name} account credentials added.')

    def create_credential(self):
        print(" ")
        print("-----Create new credential here-----")
        acc_name=input("Account name: ")
        acc_username=input("Account username: ")
        acc_password=" "

        want_password_valid=True
        while want_password_valid:        
            want_sys_password=input("Want system generated password? (Y/n): ")            
            if want_sys_password=="Y":
                want_password_valid=False
                acc_password=password_obj1.gen_password()                
                print("Your password: "+acc_password)
            elif want_sys_password=="n":
                acc_password=input("Account password: ")
                password_confirm=input("Confirm password: ")                
                if acc_password==password_confirm:                                    
                    want_password_valid=False
                else:
                    print("Passwords did not match. Try again.")
                    want_password_valid=True
            else:
                print("Invalid choice. Choose Y/n")
                want_password_valid=True    
        
        new_account=account.Account(acc_name,acc_username,acc_password)
        self.credentials_list.append(new_account)
        print(f'{acc_name} account credentials created.')

    def view_credentials(self):
        for item in self.credentials_list:
            print(f'Account: {item.acc_nm} ; Username: {item.acc_uname} ; Password: {item.acc_pass}')

    def delete_credential(self):
        pass
