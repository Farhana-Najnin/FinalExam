
from abc import ABC, abstractmethod

class Account(ABC):
    
    transaction_history=[]
    def __init__(self,name,email,address,password,type):
        self.name=name
        self.email=email
        self.accountNo = name+'123'
        self.address=address
       
        self.passW=password
        self.balance = 0
        self.type=type
        self.take_lone=0
        

    
    def changeInfo(self,name):
        self.name=name
        print(f"\n--> Name is changed of {self.accounNo}")
    
    
    def changeInfo(self,name,email,address,passW):
        self.name=name
        self.email=email
        self.address=address
        self.passW=passW
        print(f"\n--> Name ,Email,Address and Password are changed")
    def check_transaction(self):
        for item in self.transaction_history:
            print(item)
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\nWithdrawal amount exceeded")
    
    def check_available_balance(self):
        print(f"available balance {self.balance}\n")
    def loan(self,bank,amount):
        if bank.loan_status==True and self.take_lone<=2:
            print(f'bank balance-{bank.total_balance} loan_amount {amount}')
            bank.total_balance-=amount
            self.balance+=amount
            bank.loan_amount+=amount
            self.take_lone+=1
        else:
            print("Can't take loan")
        print(f'bank balance-{bank.total_balance} user balance {self.balance}')
    
    def transfer(self,user1,amount):
        if self.balance>=amount and amount>0:
            self.balance-=amount
            user1.balance+=amount
        else:
            print("not enough money in sender account")




    


class SavingsAccount(Account):
    def __init__(self,name,email,address,password,interestRate):
        super().__init__(name,email,address,password,"savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self.balance*(self.interestRate/100)
        #msg
        print("\n--> Interest is applied !")
        self.deposit(interest)
    
    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')
    def check_available_balance(self):
        print(f"available balance {self.balance}\n")


class CurrentAccount(Account):
    def __init__(self,name,password,limit):
        super().__init__(self,name,email,address,password,"current")
        self.limit=limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")
            
    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')
    def check_available_balance(self):
        print(f"available balance {self.balance}\n")


class Bank:
    
    def __init__(self) -> None:
        self.users={}
        self.total_balance=0
        self.total_loan=0
        self.loan_status=True
        self.loan_amount=0
        self.accounts=[]

    def create_account(self,name,email,address,password,type,interestRate=None,limit=None):
        if type=='savings':
            user=SavingsAccount(self,name,email,address,password,interestRate)
            self.accounts.append(user)
        elif type=='current':
            user=CurrentAccount(self,name,email,address,password,limit)
            self.accounts.append(user)

        else:
            print("Invalid account type")
            return None
        accountNo=name+email
        self.users[accountNo]=user
        return user
    def delete_account(self,accountNo):
        if accountNo in self.users:
            del self.users[accountNo]
            print(f"user account {accountNo}deleted successfully!!!")
        else:
            print("Invalid User Account number")

    def show_users(self):
        print("---User Account list ------")
        for accountNo,user in self.users.items():
            print(f'Account number-{accountNo}, Name-{user.name},Balance: {user.total_balance}')
    
    def total_available_balance(self):
        total=0
        for accountNo,user in self.users.items():
            total+=user.total_balance
        print(f'total bank balance: {total}')

    def total_loan_amount(self):
        print(f'total loan {self.loan_amount}')
        
    def OFFLoan(self):
        self.loan_status=False
    def ONLoan(self):
        self.loan_status=True

# Main program

currentUser=None
bank=Bank()

while(True):
    if currentUser==None:
        ch=input("1.Admin \n2.User \n3.exit \n")
        if ch=='admin':
            currentUser='admin'
        elif ch=='user':
            currentUser='user'
        elif ch=='exit':
            break
        else:
            print('invalid type!!')
        
            
    elif currentUser == "admin":
            password=input("enter admin password: ")
            while True:
                print("1. Delete User Account")
                print("2. View All User Accounts")
                print("3. Check Total Bank Balance")
                print("4. Check Total Loan Amount")
                print("5. loan off/On")
                print("6. Logout\n")

                option = int(input("Choose Option:"))

                if option == 1:
                    account_number = input("Enter the account number to delete: ")
                    bank.delete_account(account_number)

                elif option == 2:
                    bank.show_users()

                elif option == 3:
                    bank.total_available_balance()

                elif option == 4:
                    bank.total_loan_amount()
                elif option == 5:
                    loan=input("loan status take: ")
                    if loan == "T":
                        bank.ONLoan()
                    elif loan=="F":
                        bank.OFFLoan()
                    else:
                        print("Invalid loan status")

                elif option == 6:
                    currentUser = None
                    break

                else:
                    print("Invalid Option")  
    elif currentUser =="user":
        ch=input("\n 1.Register \n2.login \n3.exit(R/L/E)\n")
        if ch=="R":
            name=input("Name: ")
            email=input("Email: ")
            address=input("Address: ")
            pa=input("Password:")
            a=input("Savings Account or special Account (sv/c) :")
            if a=="sv":
                ir=int(input("Interest rate:"))
                currentUser=SavingsAccount(name,email,address,pa,ir)
                bank.accounts.append(currentUser)
            else:
                lm=int(input("Overdraft Limit:"))
                currentUser=CurrentAccount(name,email,address,pa,lm)
                bank.accounts.append(currentUser)
        elif ch=='L':
            no=(input("Account Number:"))
            for account in Account.accounts:
                
                if account.accountNo==no:
                    currentUser=account
                    break
                else:
                    print("Invalid Account Number") 
        else:
            break         
    else:
        print(f"\nWelcome {currentUser.name} !\n")
        
        if currentUser.type=="savings":
            
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Apply Interest")
            print("6. show balance")
            print("7. check transaction")
            print("8.taking loan ")
            print("9.transfer money")
            print("10. Logout\n")
            
            op=int(input("Chose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                name=input("Enter new name: ")
                email=input("enter new email id: ")
                address=input("enter new address: ")
                password=input("enter new password: ")
                currentUser.changeInfo(name,email,address,password)

            
            elif op==5:
                currentUser.apply_interest()
            elif op==6:
                currentUser.check_available_balance()
            elif op==7:
                currentUser.check_transaction()
                
            elif op==8:
                currentUser.loan(bank,10)
            elif op==9:
                
                ANR=input("enter reciever account number: ")
                
                amount=int(input("transferring amount: "))
                for account in bank.accounts:
                    if account.accountNo==ANR:
                        currentUser.transfer(account,amount)
                    else:
                        print("Account does not exist")


            elif op==10:
                break
                

            else:
                print("Invalid Option")
        
        else:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Logout\n")
            
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                name=input("Enter new name: ")
                email=input("enter new email id: ")
                address=input("enter new address: ")
                password=input("enter new password: ")
                currentUser.changeInfo(name,email,address,password)
            
            elif op==5:
                currentUser=None
            
            else:
                print("Invalid Option")