#Sum Of N Natural Numbers
num = int(raw_input("Enter Ur No"))
sum =0
for i in range(0,num+1):
	sum = sum+i
print "Total sum of  0 to "+ str(num) +" Numbers Is ",sum




#Sum Of N Natural Numbers Using Class

class MyClass:
	def __init__(self):
		self.num = int(raw_input("Enter Ur No :"))
		self.sum =0
	def Numbers(self):

		for i in range(0,self.num+1):
			self.sum = self.sum+i
		print "Total sum of  0 to "+ str(self.num) +" Numbers Is ",self.sum

a=MyClass()
a.Numbers()
	

