class Time:
    def __init__(self,hour:int,minute:int,second:int) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute
    
    def getSecond(self):
        return self.second
        
        
    def setHour(self,new_hour):
        self.hour = new_hour

    def setMinute(self,new_minute):
        self.minute = new_minute

    def setSecond(self,new_second):
        self.second =new_second

    def setTime(self,new_hours,new_minute,new_second):
        self.hour = new_hours
        self.minute = new_minute
        self.second = new_second

    def toString(self):
        string_time = str(self.hour).zfill(2) +":"+ str(self.minute).zfill(2)+ ":" + str(self.second).zfill(2)
        return string_time
    

    def nextSecond(self):    #12:59:59
        if self.second == 59:
            self.second = 0
            
            if self.minute == 59:
                self.minute = 0
                self.hour += 1
            else:
                 self.minute += 1
        else:
            self.second += 1
    
    def previousSecond(self): #12:00:00 , 12 : 59: 00 , 12:00:59
        if self.second == 0:
            self.second = 59
            
            if self.minute == 0:
                self.minute = 59
                self.hour -= 1
            else:
                 self.minute -= 1
        else:
            self.second -= 1

        

      
       
            
    








test = Time(1,30,15)

print(test.getHour())

print(test.getMinute())

print(test.getSecond())

test.setHour(2)

test.setMinute(5)

test.setSecond(9)

test.setTime(0,59,59)

test.nextSecond()     

# test.previousSecond()

print(test.toString())
        
