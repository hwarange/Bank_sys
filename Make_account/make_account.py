def make_account():
    print('[계좌 계설]')
    id = input()
    name = input()
    money = input()
    account_list.append(Account(id, money, name))
