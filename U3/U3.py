class Date:
    def __init__(self, day, month, year):
        if month > 12 or month > 31:
            print("Bunday vaqt yo'q ! ")
            exit()
        if month == 2 and month > 29 :
            print("Bunnday vaqt yo'q !")
            exit()
        self.day = day
        self.month = month
        self.year = year
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year
    
    def setDay(self, new_day):
        self.day = new_day
    def setMonth(self, new_month):
        self.month = new_month
    def setYear(self, new_year):
        self.year = new_year
    def setDate(self, new_day, new_month, new_year):
        self.day = new_day
        self.month = new_month
        self.year = new_year
    def toString(self):
        day = self.day
        month = self.month
        year = self.year
        string_date = str(day).zfill(2) +"."+ str(month).zfill(2)+ "." + str(year)

        return string_date
    
My_data = Date(8,7,2024)


print(My_data.getDay())

print(My_data.getMonth())

print(My_data.getYear())


My_data.setDay(5)

My_data.setMonth(8)

My_data.setYear(2025)

My_data.setDate(9,3,2026)

print(My_data.toString())