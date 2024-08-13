def show_all_account_information():
    for i in account:
        print(f'계좌ID: {i.account_id}')
        print(f'이    름: {i.customer_name}')
        print(f'잔    액: {i.balance}')