class User:

    users_list=[]

    def __init__ (self, username, password):
        self.username=username
        self.password=password

    @classmethod
    def add_user(cls, new_user):
        cls.users_list.append(new_user)