
class Account():
    def __init__(self, account_id, balance, customer_name):
        self.account_id = account_id
        self.balance = balance
        self.customer_name = customer_name

    def get_account_id(self):
        return self.account_id
    
account = []
num_of_accounts = 0

def deposit_money():
    print('[입    금]')
    id = input('계좌ID: ')
    for i in range(len(account)):
        if account[i].account_id == id:
            money = input('입금액: ')
            account[i].balance -= money
        else:
            print('유효하지 않는 ID입니다.')
    







def main():

    
    """Main function to run the banking system."""
    while True:
        show_menu()
        choice = menu_input()
        print()

        if choice == 1:
            make_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            show_all_account_information()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name__ == "__main__":
    main()