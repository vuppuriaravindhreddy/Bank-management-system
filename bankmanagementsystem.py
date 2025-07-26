
import random
import stdiomask
class bank:
    def __init__(self,bankname,location,balance):
        self.bankname=bankname
        self.location=location
        self.balance=balance
    def account_creation(self):
        self.surname=input("enter your surname:")
        self.name=input("enter your name:")
        self.date_of_birth=int(input("enter your year:"))
        self.gender=input("enter your gender:")
        self.address=input("enter your address:")
        pancard_number=stdiomask.getpass(prompt="enter your pan card number:",mask="*")
        self.pinnumber=input("set your pin number:")
        if len(pancard_number)>10:
            print("entered invalid size pan card no")
        else:
            print(f"your account created successfully and your account no is{random.randint(1234556789, 2233456789)}")
    def deposit(self,amount):
        pin=stdiomask.getpass(prompt="enter your pin:",mask="*")
        if (self.pinnumber)==pin:
            if amount<=0:
                print("please enter the positive amount to deposit")
            else:
                self.balance+=amount
                print(f"your amount deposited successfully and deposited amount is {amount}")
        else:
            print("you entered incorrect pin!")
class bank2(bank):
    def cash_with_draw(self,amount):
        pin=stdiomask.getpass(prompt="enter your pin:",mask="*")
        if (self.pinnumber)==pin:
            if amount>self.balance:
                print("insufficient balance")
            elif self.balance==0:
                print("there is zero balance in your account")
            else:
                self.balance-=amount
                print(f"the cash successfully withdrawed.withdraw cash is {amount}")
        else:
            print("entered inccorect pin")
    def balance_enquiry(self):
        pin=stdiomask.getpass(prompt="enter your pin:",mask="*")
        if (self.pinnumber)==pin:
            print(f"the available balance in your account is {self.balance}")
        else:
            print("entered inccorect pin")
    def exit(self):
        print(f"thank you for choosing our atm!")

class bank3(bank2):
    def mini_statement(self):
        print(f"bankname:{bankname}")
        print(f"location:{location}")
        print(f"balance:{self.balance}")

user_name="aravindhreddy"
pass_word="12345"
username=input("enter your username:")
password=input("enter your password:")
if user_name==username and pass_word==password:
    bankname=input("enter the bankname:")
    location=input("enter the location:")
    user=bank3(bankname,location,0)
else:
    print("invalid user name or password!")
    exit()

while True:
    print("1.Account Creation")
    print("2.Deposit")
    print("3.withdraw")
    print("4.balance")
    print("5.exit")
    option=int(input("enter your choice:"))
    if option==1:
        user.account_creation()
    elif option==2:
        amount=float(input("enter the amount:"))
        user.deposit(amount)
    elif option==3:
        amount=float(input("enter the amount:"))
        user.cash_with_draw(amount)
    elif option==4:
        user.balance_enquiry()
    elif option==5:
        user.exit()
        break
    else:
        print("entered invalid choice!please try agin")
