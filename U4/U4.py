class Employee:
    def __init__(self,id:int , firstName:str , lastName:str , salary:int ) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getName(self):
        return f"{self.getFirstName()} {self.getLastName()}"

    def getSalary(self):
        return self.salary

    def setSalary(self,new_salary):
        self.salary = new_salary

    def getAnnualSalary(self,):
        self.salary = self.salary * 12

    def raiseSalary(self,percent:int):
        self.salary *= (1 + percent / 100)
        return self.salary

    def toString(self):
        return f"ID = {self.id}, Name = {self.firstName},lastName = {self.lastName},salary = {self.salary}"
    
        

    
s1 = Employee(24470,"Sarvar","Qodirov",5600)


print(s1.getID()) 
print(s1.getFirstName())
print(s1.getLastName())
print(s1.getName())
print(s1.getSalary())
s1.setSalary(5700)
s1.raiseSalary(5)
print(s1.toString())

