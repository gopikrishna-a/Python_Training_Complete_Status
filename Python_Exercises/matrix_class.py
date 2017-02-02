class matrix():
	def __init__(self):

		self.l1=input('enter the size(m*n) of 1st matrix\n')
		self.mat1_row=self.l1*self.l1
		self.l2=input('enter the size(m*n) of 2st matrix\n')
		self.mat2_row=self.l2*self.l2
		self.mat1=[]
		self.mat2=[]
		self.res=[]
	
	def mat(self):
		if (self.mat1_row==self.mat2_row):
			for i in range(self.mat1_row):
				x=input("enter the value of 1st matrix\n")
				self.mat1.append(x)
			print self.mat1
			for i in range(self.mat2_row):
				x=input("enter the value of 2st matrix\n")
				self.mat2.append(x)
			print self.mat2
		else:
			print "matrix not matched"



		self.res=[x+y for x,y in zip(self.mat1,self.mat2)]
		print "addtion of two matrix",self.res

		self.res=[x-y for x,y in zip(self.mat1,self.mat2)]
		print "subtraion  of two matrix",self.res

		self.res=[x*y for x,y in zip(self.mat1,self.mat2)]
		print "multiflication  of two matrix",self.res


a=matrix()
a.mat()
