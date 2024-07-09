# U8:

# Book nomli class yarating va uning property 
# elementlari quyidagilardan iborat:

# -    Name(Kitob nomi);
# -    Page_count(Kitobning sahifalar soni);
# -    Price(Kitobning narxi).
# Ushbu classga tegishli 5ta obyekt yarating va ularni ma’lumotlarni 
# foydalanuvchi tomonidan kiriting.

# Sizning vazifangiz quyidagilardan iborat bo‘lgan har bir obyekt uchun metodlar
#  yaratish:

# 1)    Barcha kitoblarning sahifalar sonini 10taga oshiring.
# 2)    Agar sahifalar soni 100tadan ko‘p bo‘lsa(oshirishdan keyin),
# ushbu kitobning narxini 2 barobar kamaytiring.


class Book :
    def __init__(self,name,page,price) -> None:
        self.name = name
        self.page = page
        self.price = price

    def plus_page(self):
        self.page += 10

    def check_page(self):
        if self.page > 100 :
            self.price /= 2

    def fulldata(self):
        print(f"Nomi:{self.name}")
        print(f"Saxifasi:{self.page}")
        print(f"Narxi:${self.price}")
        print()

        
book1 = Book("Python Programming", 300, 50)
book2 = Book("Deep Learning Basics", 150, 80)
book3 = Book("Data Structures in C++", 200, 70)
book4 = Book("Machine Learning Algorithms", 120, 90)
book5 = Book("Web Development with Django", 400, 120)


books = [book1,book2,book3,book4,book5]

for book in books:
    book.plus_page()


for book in books:
    if book.page > 100:
        book.check_page()

for book in books:
    book.fulldata()