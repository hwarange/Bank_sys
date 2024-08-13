
def deposit_money():
    print('[입    금]')
    id = input('계좌ID: ')
    for i in range(len(account)):
        if account[i].account_id == id:
            money = input('입금액: ')
            account[i].balance -= money
        else:
            print('유효하지 않는 ID입니다.')