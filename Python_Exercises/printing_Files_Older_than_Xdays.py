
import os
import time
import sys
from datetime import date
from datetime import datetime,timedelta


arg1=sys.argv[0]
arg2=sys.argv[1]
#arg3=sys.argv[2]
tdy=datetime.today()
print "today date is ---  ",tdy 

ago=tdy-timedelta(days=30)
print "30 days back date is ---  ",ago

cwd=os.getcwd()  # current working directory
lfs=os.listdir(cwd) # list of file in that current directory
#print lfs
lis=[]
lis1=[]

if arg1:
	print "name of the file\n",arg1
	print "\n"

for i in lfs:
	
	file_time=datetime.fromtimestamp(os.path.getctime(i))
	#print file_time
	if file_time<ago:
		#print i
		des=datetime.fromtimestamp(os.path.getctime(i))
		lis.append(des)
		path=os.path.realpath(str(i))
		lis1=sorted(lis)
		
		if arg2=="path":
			#print "path of the files"	
			print path
if arg2=="date":
	for j in lis1:
		#print "date of the files\n"
		print j

if arg2=="deletedate":
	for j in lis1:
		choice=raw_input("do u want delete date\n")
		if choice=="y":
			newlis=lis1.remove(j)
			print "deleted date is ",j
		else:
			print "error"
				

	
