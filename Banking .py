import random as rd
import datetime as dt



transaction_log=[]

Name=input('Enter your full name :')
Phone_no=int(input('Enter a mobile no :'))
acc_no=rd.randint(10000000,99999999)
print('Account number : ',acc_no)
PIN=int(input('Create a pin : '))
Curr_Bal=float(input('Enter a balance :'))


acc_info=int(input('enter your acc_no :'))
if acc_info==acc_no:
    PIN2=int(input('enter your PIN :'))
    if PIN==PIN2:
        print('acc_no : ',acc_no)
        print('Name : ',Name)
        print('Login Succesfully!!')
    else:
        print('incorrect PIN??')
else:
    print('Not Found!!')

def cur_bal():
    print("Current balance :",Curr_Bal)

def Deposite():
    global Curr_Bal
    dep_amo=float(input('Enter a amount :'))
    Curr_Bal=Curr_Bal+dep_amo 
    timestamp=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_log.append(f'[{timestamp}] deposit:+{dep_amo} balance:{Curr_Bal}')
    print("now current balance : ",Curr_Bal)

def withdraw():
    global Curr_Bal
    print("current balance : ",Curr_Bal)
    withdraw_amount=float(input("enter a withdraw_amount :"))
    if withdraw_amount> Curr_Bal:
        print("insufficient Bal!!")
    else:
        Curr_Bal=Curr_Bal-withdraw_amount
        timestamp=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction_log.append(f'[{timestamp}] withdraw_amount:+{withdraw_amount} balance:{Curr_Bal}')
        print("now current balance :",Curr_Bal)

def transaction():
    global Curr_Bal
    reciver_acc_no=int(input("enter a reciver acc number :"))
    transfer_amount=float(input('enter a transaction amount :'))
    if transfer_amount>Curr_Bal:
        print("insufficent Bal")
    else:
        Curr_Bal=Curr_Bal-transfer_amount
        timestamp=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction_log.append(f'[{timestamp}] transaction:+{transfer_amount} balance:{Curr_Bal}')
        print(" now current balance :",Curr_Bal)

def ChangePIN():
    global Curr_PIN
    Curr_PIN=int(input("enter a current PIN :")) 
    if Curr_PIN!=PIN:
        print("invalid PIN!!")
    else:
        Enter_NEW_PIN=int(input("enter a NEW PIN :"))
        Confirm_NEW_PIN=int(input("enter a confirm PIN :"))
        if Enter_NEW_PIN==Confirm_NEW_PIN:
            PIN=Confirm_NEW_PIN
            print('your NEW PIN :',PIN)
        else:
            print("PIN dosen't match!!")


def transaction_history():
    if len(transaction_log)==0:
        print("no history")
    else:
        print("--transaction history")
        for entry in transaction_log:
            print('entry')

def logout():
    print("logging out!!!!!!")
    return True


acc_information={'Name':Name,
             'Phone_no':Phone_no,
             'acc_no':acc_no,
             'PIN':PIN,
             'Curent Balance':Curr_Bal,
             }

while True:
    print("1:check balance\n 2:Deposit\n 3:withdraw\n 4:Transaction \n 5:Transaction History\n 6:Change PIN\n 7:Logout")
    status=int(input("you choose from above:"))
    match status:
        case 1:
            cur_bal()
        case 2:
            Deposite()
        case 3:
            withdraw()
        case 4:
            transaction()
        case 5:
            transaction_history()
        case 6:
            ChangePIN()    
        case 7:
            logout()
            break
        case _:
            print("invalid option!!!")
            
print(acc_information)



