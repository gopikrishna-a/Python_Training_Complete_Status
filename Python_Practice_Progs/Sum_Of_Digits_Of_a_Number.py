#Sum Of Digits Of Number
num  = int(raw_input("Enter Ur Number:"))
temp = num
tsum = 0
while num > 0:
	rem = num%10
	tsum = tsum+rem
	num = num//10
print "Sum of Digits of "+str(temp)+" is :",tsum
	

#Sum Of Digits Of Number Using Class
class MyClass:
	def __init__(self):
		self.num  = int(raw_input("Enter Ur Number:"))
		self.temp = num
		self.tsum = 0
	def Sum_Of_Digits(self):
		while self.num > 0:
			self.rem = self.num%10
			self.tsum = self.tsum+self.rem
			self.num = self.num//10
		print "Sum of Digits of "+str(self.temp)+" is :",self.tsum


a = MyClass()
a.Sum_Of_Digits()
