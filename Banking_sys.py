import random as rd
import datetime as dt

accounts = {}   

def create_account():
    name = input("Enter your full name: ")
    phone_no = input("Enter a mobile no: ")
    acc_no = rd.randint(10000000, 99999999)

    while acc_no in accounts:          
        acc_no = rd.randint(10000000, 99999999)

    pin = int(input("Create a PIN: "))
    curr_bal = float(input("Enter an opening balance: "))

    accounts[acc_no] = {
        "name": name,
        "phone_no": phone_no,
        "pin": pin,
        "balance": curr_bal,
        "history": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number is:", acc_no)
    
def login():
    acc_no = int(input("Enter your account number: "))

    if acc_no not in accounts:
        print("Account not found!\n")
        
    pin = int(input("Enter your PIN: "))

    if accounts[acc_no]["pin"] != pin:
        print("Incorrect PIN!\n")
    else:
        print("\nLogin successful! Welcome,", accounts[acc_no]["name"], "\n")

    account_menu(acc_no)



def check_balance(acc_no):
    print("Current balance : ", accounts[acc_no]["balance"])


def deposit(acc_no):
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Enter a valid amount!")
    else:
        accounts[acc_no]["balance"] += amount
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] Deposit: +{amount} | Balance: {accounts[acc_no]['balance']}"
        accounts[acc_no]["history"].append(entry)

    print("Deposit successful , New balance:", accounts[acc_no]["balance"])

def withdraw(acc_no):
    print("Current balance:", accounts[acc_no]["balance"])
    amount = float(input("Enter withdraw amount: "))

    if amount <= 0:
        print("Enter a valid amount!")
        
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] Withdraw: -{amount} | Balance: {accounts[acc_no]['balance']}"
        accounts[acc_no]["history"].append(entry)
        print("Withdrawal successful. New balance:", accounts[acc_no]["balance"])


def transfer(acc_no):
    receiver_acc_no = int(input("Enter receiver's account number: "))
    if receiver_acc_no == acc_no:
        print("You cannot transfer to your own account!")
    else:
        amount = float(input("Enter transfer amount: "))
        if amount <= 0:
            print("Enter a valid amount!")
        elif amount > accounts[acc_no]["balance"]:
            print("Insufficient balance!")
        else:
            accounts[acc_no]["balance"] -= amount
            timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Transfer_entry = f"[{timestamp}] Transfer: - {amount} to {receiver_acc_no} to {acc_no}| Balance: {accounts[acc_no]['balance']}"
            accounts[acc_no]["history"].append(Transfer_entry)
            print("Transfer successful. New balance:", accounts[acc_no]["balance"])


def transaction_history(acc_no):
    history = accounts[acc_no]["history"]

    if len(history) == 0:
        print("No transactions yet.")
    else:
        print("Transaction History ")
        for entry in history:
            print(entry)
        
def change_pin(acc_no):
    curr_pin = int(input("Enter your current PIN: "))

    if curr_pin != accounts[acc_no]["pin"]:
        print("Incorrect current PIN!")
    else:
        new_pin = int(input("Enter a new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))
        if new_pin == confirm_pin:
            accounts[acc_no]["pin"] = new_pin
            print("PIN changed successfully!")
        else:
            print("PIN do not match!")


def logout():
    print("Logging out...\n")
    return True

def account_menu(acc_no):
    while True:
        print("ACCOUNT MENU")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History ")
        print("6. Change PIN ")
        print("7. Logout")
        

        status = int(input("Choose an option: "))
        match status:
            case 1:
                check_balance(acc_no)
            case 2:
                deposit(acc_no)
            case 3:
                withdraw(acc_no)
            case 4:
                transfer(acc_no)
            case 5:
                transaction_history(acc_no)
            case 6:
                change_pin(acc_no)
            case 7:
                if logout():
                    break
            case _:
                print("Invalid option, try again.")

        print() 

def main_menu():
    while True:
        print("MAIN MENU")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

    
        choice = int(input("Choose an option: "))
        match choice:
            case 1:
                create_account()
            case 2:
                login()
            case 3:
                print("Thank you for using the Banking System. Goodbye!")
                break
            case _:
                print("Invalid option, try again.\n")

if __name__ == "__main__":
    main_menu()
