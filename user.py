class User:

    users_list=[]

    def __init__ (self, username, password):
        self.username=username
        self.password=password

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