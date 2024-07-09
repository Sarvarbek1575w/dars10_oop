
# U7:

# Mashina nomli class yarating. Ushbu classning elementlari nomi, 
# turi (yengil, yuk avtomobili), narxi, ishlab_chiqarilgan_yili. Mashinaning 
# malumot nomli methodi bor unda mashina xaqida malumot chiqib keladi.
# 10 ta mashina xaqida malumot berilgan mashinalarni 
# ishlab chiqarilgan yili bo’yicha saralab ekranga chop eting. Mashinani
#  narxi kiritilmaganda default 4.000$ qiymatni berib keting.


class Mashina:
    def __init__(self, turi, yili, narxi = 4000) -> None:
        self.turi = turi
        self.narxi = narxi 
        self.yili = yili

    def malumot(self):
        print(f"Turi:{self.turi}")
        print(f"Yili: {self.yili}")
        print(f"Narxi:${self.narxi}")
        print() 
        
mashina1 = Mashina("matiz", 2009, 3000)
mashina2 = Mashina("tico", 2007, 1500)
mashina3 = Mashina("nexia1", 2010, 4000)
mashina4 = Mashina("damas", 2011, 3000)
mashina5 = Mashina("cobalt", 2015, 5000)
mashina6 = Mashina("Gentra", 2017, 7000)
mashina7 = Mashina("malibu", 2018, 12000)
mashina8 = Mashina("Onix", 2019, 15000)
mashina9 = Mashina("byd", 2024, 14000)

lst = [mashina1, mashina2, mashina3, mashina4, mashina5, mashina6, mashina7, mashina8, mashina9]

lst_sorted = sorted(lst, key=lambda x: x.yili if x.yili else 0)

for mashina in lst_sorted:
    mashina.malumot()


