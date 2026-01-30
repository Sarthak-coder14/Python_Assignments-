class BankAccount:
    
    ROI = 10.5   
    
    def __init__(self, BankName, BankAmount):
        self.Name = BankName
        self.Amount = BankAmount
         
    
    def Display(self):
        print("Account Namme : ",self.Name)
        print("Current Balance : ",self.Amount)

    def Deposit(self,Deposite_Amt):

        self.Amount = self.Amount + Deposite_Amt
        print("Ammount is deposited")

    def Withdraw(self,Withdraw_Atm):
        if Withdraw_Atm <= self.Amount:
            self.Amount = self.Amount - Withdraw_Atm

        else :
            print("Insufficient balance.")

    def CalculateInterest(self,):
        Interest  = (self.Amount * BankAccount.ROI ) / 100
        return Interest
    


def main():
    Obj1 = BankAccount("Janu", 10000)
    Obj1.Display()
    Obj1.Deposit(2000)
    Obj1.Display()
    print("Interest is  :", Obj1.CalculateInterest())

    print()

    Obj2 = BankAccount("Pranit", 5000)
    Obj2.Display()
    Obj2.Withdraw(8000)
    print("Interest is  :", Obj2.CalculateInterest())



if __name__ == "__main__":
    main()