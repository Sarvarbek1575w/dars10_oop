class Account:
    def __init__(self,id:str, name:str, balance:int) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def get_ID(self):
        return self.id
    def getName(self):
        return self.name
    def getBalance(self):
        return self.balance
    def credit(self,amount):
        self.balance += amount
        return self.balance
    def debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("amound exceded balance")
            return self.balance
      
    def transferTo(self,reciever_account,amount:int):
        if amount <= self.balance and amount > 0 :
            self.balance -= amount
            reciever_account.balance += amount
            print(f"${amount} Transfered from {account1.getName()} to {account2.getName()}")
        else:
            print("Transfer failed >Insufficient funds or invalid amount")

user = Account("ID007","Sarvar",15)
print(user.get_ID())
print(user.getName())
print(user.getBalance())
print(user.credit(400))
print(user.debit(300))


account1 = Account("ID24470","Sarvar",200)
account2 = Account("ID32422","Aziz",40)

print(f"Before transfer: {account1.get_ID()} Balance: ${account1.getBalance()}")
print(f"Before transfer: {account2.get_ID()} Balance: ${account2.getBalance()}")

account1.transferTo(account2,30)

print(f"After Transfer: {account1.get_ID()} Balance:${account1.getBalance()}")
print(f"After Transfer: {account2.get_ID()} Balance:${account2.getBalance()}")




