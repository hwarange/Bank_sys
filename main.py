import show_all_account_information
import deposit_money
import make_account
import screen_set
import withdraw_money

    
account = []
num_of_accounts = 0


def menu_input():
    int(input('선택: '))


def main():

    
    """Main function to run the banking system."""
    while True:
        screen_set.show_menu()
        choice = menu_input()
        print()

        if choice == 1:
            make_account.make_account()
        elif choice == 2:
            deposit_money.deposit_money()
        elif choice == 3:
            withdraw_money.withdraw_money()
        elif choice == 4:
            show_all_account_information.show_all_account_information()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name__ == "__main__":
    main()