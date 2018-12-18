class studentCard :
	def __init__(self, number , name , en):
		self.en = en
		self.number = number
		self.name = name

	def setter(self , en):
		self.en += en

	def getter(self):
		return self.en

	def getName(self):
		return self.name

students = [studentCard(183301,"Aaoki" , 500) , studentCard(183302 , "Suzuki" , 1000)]

a = 100

#for student in students:
#	student.setter(a)
#	print(student.getter())
#	print(student.getName())
#	a+=100