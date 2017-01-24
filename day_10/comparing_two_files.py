#Python script to compare the attached two files and find out status 'ok' and 'FAIL'
#Created By A.gopikrishna


import re
import sys
arg1=sys.argv[1]
arg2=sys.argv[2]
class MyClass:

	def __init__(self,src,des):
		self.src=open(arg1)
		self.des=open(arg2)

#Task-1		Total Number Of Lines Starts With tempest In 1st File

	def Extracting(self):
		self.st0=''
		self.st1=''
		self.dt0=''
		self.dt1=''
		self.mydict1={}
		self.mydict2={}
		self.mylist1= []
		self.mylist2 = []
		count=0
		
		try:
		   for line in self.src:
			sq = re.search(r'(tempest.*)',line,re.IGNORECASE)
			count+=1
			if sq:
			  result = str(sq.group())
			  result_split = result.split(' ... ')
			  self.st0=result_split[0]
			  self.st1=result_split[1]

			  result_strip = self.st1.strip('\r')
			  self.mydict1[self.st0]=result_strip 

			  self.mylist1.append(str(self.st0)+' ... '+str(result_strip))
		   #print count
		   

		except IndexError:
			pass
		print "Total number of lines starting with 'tempest' in first  file : ",len(self.mydict1)

#Task-2		Total Number Of Lines Starts With tempest In 2nd File

		try:
		   for line in self.des:
			sq = re.search(r'(tempest.[a-zA-Z](.*))',line,re.MULTILINE|re.IGNORECASE)
			if sq:
			  result = str(sq.group())
			  result_split = result.split(' ... ')
			  self.dt0=result_split[0]
			  self.dt1=result_split[1]

			  result_strip = self.dt1.strip('\r')
			  self.mydict2[self.dt0]=result_strip 

			  self.mylist2.append(str(self.dt0)+' ... '+str(result_strip))

		except IndexError:
			pass
		print "Total number of lines starting with 'tempest' in second  file  : ",len(self.mydict2)

#Task-3		Total number of lines 'tempest' to '...' matching status same  ( both are 'ok' or both are 'FAIL' )

	
	def same_status(self):
		count=0
		file=open("same_status.txt",'w')#Task-8 Create a file which has lines 'tempest' to '...' matching status same 
		for i in self.mylist1:
			for j in self.mylist2:
				if i==j:
					file.writelines(i+'\n')
					count+=1
		file.close()
		print "Total number of lines 'tempest' to '...' matching status same :", count
		

	def different_status(self): 
		count=0
		file=open("different_status.txt",'w')#Task-9 Create a file which has lines 'tempest' to '...' matching status differ
		for key in self.mydict1:
			for key1 in self.mydict2:
				if (key==key1):
					if(self.mydict1[key]!=self.mydict2[key1]):
						file.writelines(key+'\n')#writing to file
						count=count+1
		file.close()
		print "Total number of lines 'tempest' to '...' matching status differs :",count
		
#Task-5 Total number of lines 'tempest' to '...' matching status may be anything ( the status is neither 'ok' not 'FAIL')

	def anything(self):
		  
		  file=open("any_status.txt",'w')#Task-12 file creation matching status may be anything(the status is neither 'ok' not 'FAIL')
		  count=0
		  for key in self.mydict1:
			 if (self.mydict1[key]!='ok')&(self.mydict1[key]!='FAIL'):
			   file.writelines(key+'\n')
			   count+=1
		
		  count_=0
		  for key in self.mydict2:
			if(self.mydict2[key]!='ok')&(self.mydict2[key]!='FAIL'):
			  file.writelines(key+'\n')
			  count_=count_+1
		  file.close()
		  print "Total number of lines 'tempest' to '...' matching status may be anything :",count+count_

#Task-6  Total number of lines 'tempest' to '...' available in first not in second
		  
	def total_in_src(self):
		count=0
		file=open("fns.txt",'w')#Task-10  Create a file which has lines 'tempest' to '...' available in first not in second
		for key in self.mydict1:
			if self.mydict2.has_key(key):
				pass
			else:
				file.writelines(key+'\n')
				count=count+1
		file.close()
		print "Total number of lines 'tempest' to '...' available in first not in second :",count

#Task-7 Total number of lines 'tempest' to '...' available in second not in first
		
	def total_in_des(self):
		count=0
		file=open("snf.txt",'w')#Task-11  Create a file which has lines 'tempest' to '...' available in second not in first
		for key in self.mydict2:
			if self.mydict1.has_key(key):
				pass
			else:
				file.writelines(key+'\n')
				count=count+1
		file.close()
		print "Total number of lines 'tempest' to '...' available in second not in first :",count


		
a=MyClass(arg1,arg2)

a.Extracting()
a.same_status()
a.different_status()
a.anything()
a.total_in_src()
a.total_in_des()
