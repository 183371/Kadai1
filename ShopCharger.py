import StudentCard as insertedStudentCard 
class shopCharger:
	
	
	def __init__(self , card):
		self.card = card

	def chargeMoney(self , en):
		if self.card is not None:
			self.card.setter(en)
		else:
			print("Student ID card is not inserted")

	def printAccountBalance(self):
		print(self.card.getName())
		print(self.card.getter())
		

#card = insertedStudentCard.studentCard("Taro")
#a = shopCharger(card)
#a.chargeMoney(1000)
