
class Account():
    def __init__(self, account_id, balance, customer_name):
        self.account_id = account_id
        self.balance = balance
        self.customer_name = customer_name

    def get_account_id(self):
        return self.account_id
    
account = []
num_of_accounts = 0

def show_all_account_information():
    for i in account:
        print(f'계좌ID: {i.account_id}')
        print(f'이    름: {i.customer_name}')
        print(f'잔    액: {i.balance}')







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