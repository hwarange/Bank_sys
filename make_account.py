class Account():
    def __init__(self, account_id, balance, customer_name):
        self.account_id = account_id
        self.balance = balance
        self.customer_name = customer_name

    def get_account_id(self):
        return self.account_id
    
account = []
num_of_accounts = 0

def make_account():
    print('[계좌 계설]')
    id = input()
    name = input()
    money = input()
    account.append(Account(id, money, name))
