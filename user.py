import credentials
class User:

    users_list=[]

    def __init__ (self, username, password):
        self.username=username
        self.password=password
        self.credential=credentials.Credentials()

    @classmethod
    def add_user(cls, new_user):
        cls.users_list.append(new_user)

    @classmethod
    def check_login(cls, login_name, login_pass):
        for user in cls.users_list:
            if user.username==login_name:
                if user.password==login_pass:
                    return True
        return False

    @classmethod
    def return_user(cls, username, password):
        for user in cls.users_list:
            if user.username==username:
                if user.password==password:
                    return user