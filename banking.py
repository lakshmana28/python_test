from abc import ABCMeta,abstractmethod
from random import randint

class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0
class SavingAccount():
    def __init__(self):
        self.savingsAccount={}
    def CreateAccount(self,name,initialDeposit):
        self.accountNumber=randint(10000,99999)
        self.savingsAccount[self.accountNumber]=[name,initialDeposit]
        print('account ceated',self.accountNumber)
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0]==name:
                print('Authentication successful')
                self.accountNumber=accountNumber
                return True
            else:
                print('Authentication failed')
                return False
        else:
            print('Not a valid account number')
            return False

    def withdraw(self,withdrawalAmount):
        if withdrawalAmount>self.savingsAccount[self.accountNumber][1]:
            print('insufficient')
        else:
            self.savingsAccount[self.accountNumber][1]-=withdrawalAmount
            print('withdrwal')
            self.displayBalance()

    def deposit(self,depositAmount):
        self.savingsAccount[self.accountNumber][1]=+depositAmount
        print('deposit was successful')
        self.displayBalance()

    def displayBalance(self):
        print('available',self.savingsAccount[self.accountNumber][1])
savingsAccount=SavingAccount()

while True:
    print('Enter 1 to create a new ac ')
    print('Enter 2 to access an existing ac')
    print('Enter 3 to exit')
    userChoice=int(input())
    if userChoice is 1:
        print('Enter Your name: ')
        name=input()
        print('Enter the initial deposit')
        deposit=int(input())
        savingsAccount.CreateAccount(name,deposit)
    elif userChoice is 2:
        print('Enter Your name: ')
        name = input()
        print('Enter account number')
        accountNumber = int(input())
        authenticationstatus=savingsAccount.authenticate(name, accountNumber)
        if authenticationstatus is True:
            while True:
                print('Enter 1 to withdrwa')
                print('Enter 2 to deposit')
                print('Enter 3 to bal check')
                print('Enter 4 to go back to previous menu')
                userChoice=int(input())
                if userChoice is 1:
                    print('Enter withdrwal amount')
                    withdrawalAmount=int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print('Enter deposit amount')
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                   savingsAccount.displayBalance()
                elif userChoice is 4:
                    break

    elif userChoice is 3:
        quit()


