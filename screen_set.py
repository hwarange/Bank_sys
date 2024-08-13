account_list = []
num_of_accounts = 0

class Account()


def show_menu():
    print(
        '''
-----Menu------
      1. 계좌개설
      2. 입    금
      3. 출    금
      4. 계좌정보 전체 출력
      5. 프로그램 종료
      '''
    )


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