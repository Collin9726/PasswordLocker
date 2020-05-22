import user
import string
import random
class Credentials:
    
    password_letters=list(string.ascii_letters)
    password_nums=list(string.digits)
    password_symbols=["#","@","&","$","%"]
    password_chars=[]
    password_chars.extend(password_letters)
    password_chars.extend(password_nums)
    password_chars.extend(password_symbols)

    @classmethod
    def gen_password(cls):
        sys_password="".join(random.sample(cls.password_chars, k=10))               
        return sys_password

# obj=Credentials()
# print(obj.gen_password())
