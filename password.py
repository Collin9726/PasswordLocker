import string
import random
import pyperclip
class Password:
    """
    Class that generates system given passwords.
    """    
    password_letters=list(string.ascii_letters)
    password_nums=list(string.digits)
    password_symbols=["#","@","&","$","%"]
    password_chars=[]
    password_chars.extend(password_letters)
    password_chars.extend(password_nums)
    password_chars.extend(password_symbols)

    @classmethod
    def gen_password(cls):
        """
        Method to generate system given passwords.
        
        Returns:
            System generated password
        """
        pass_length=10
        num_valid=True
        while num_valid:
            try:
                pass_length=int(input("Enter password length (at least 5): "))
                if pass_length<5:
                    print("**Length should be at least 5. Try again.")
                    num_valid=True
                else:
                    num_valid=False
            except ValueError:
                print("**Invalid input. Use numbers.")
                num_valid=True
            
        sys_password="".join(random.sample(cls.password_chars, k=pass_length))
        pyperclip.copy(sys_password)               
        return sys_password
 
