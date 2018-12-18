import StudentCard as card
import ShopCharger as shop
class mainShopCharger:
	def __init__(self):
		self.shop = None
		self.StudentCard1 = None
		self.StudentCard2 = None

	def main(self):
		self.StudentCard1 = card.students[0];
		self.StudentCard2 = card.students[1];

	def insertStudentCard(self , i , en):
		if i == 1:
			self.shop = shop.shopCharger(self.StudentCard1)
		elif i == 2:
			self.shop = shop.shopCharger(self.StudentCard2)
		self.shop.chargeMoney(en)
		self.shop.printAccountBalance()

a = mainShopCharger()
a.main()

#2nd	2000 yen charge
a.insertStudentCard(2 , 2000)
#1		1000 yen charge
a.insertStudentCard(1 , 1000)
#1		500 yen to use
a.insertStudentCard(1 , 500)
#2nd	2400 yen to use
a.insertStudentCard(2 , -2400)