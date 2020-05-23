class Account:
    """
    Class that generates new instances of account credentials to be stored.
    """
    def __init__(self, acc_nm, acc_uname, acc_pass):
        self.acc_nm=acc_nm
        self.acc_uname=acc_uname
        self.acc_pass=acc_pass