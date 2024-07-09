class Rectangle:
    def __init__(self,height,width) -> None:
        self.height = height
        self.width = width

    def get_height(self):
        return self.height
    
    def set_height(self,new_height):
        self.height = new_height

    def get_width(self):
        return self.width
    
    def set_width(self,new_width):
        self.width = new_width

    def get_area(self):
        yuza = self.width * self.height
        return yuza
    def get_peremetr(self):
        peremetr = (self.width + self.height) * 2
        return peremetr
    
    def get_info(self):
        return f"Bo'yi:{self.get_height()},Eni:{self.get_width()},Yuzasi:{self.get_area()},Peremetr:{self.get_peremetr()}"
    


test = Rectangle(10,20)


print(test.get_height())
test.set_height(12)

print(test.get_width())
test.set_width(22)

print(test.get_area())

print(test.get_peremetr())

print(test.get_info())
















                     
    