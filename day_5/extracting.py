#!/usr/bin/python
import re
import sys
import mysql.connector
file=open("diag.out")#/home/asm/Downloads/diag.out
print(file)
list_of_lines= []
mylist=[]
for line in file:
    res = re.match("----- APmgr info: apmgrinfo -a", line , re.M|re.I)
    if res:
	for line in file:
	    list_of_lines.append(line)
	    #print(list)
	    res1=re.match("65 APs are connected", line, re.M|re.I)
 	    if res1:
		break
print("file extracted")
for n in list_of_lines:
    	#print(n)
	if n == "\n":
		print "_________________________"

aps = []

ap = []
for line in list_of_lines:
	
	if line != "\n":
		ap.append(line)
	else:
		ap = "".join(ap)
		aps.append(ap)
		ap = [] 

print len(aps)

 

for ap in aps:
	print ap
	print "_______________________"
	print ap[8:25]
	print ap[28:43]




#Extracting mac
import re

file = open('diag.out','rb').read()
#[0-9A-F]{2}[:-]){5}([0-9A-F]{2}
p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
a = re.findall(p,file)
#print a
for i in a:
    print i


#ipv4

file = open('diag.out','rb').read()
#p = re.compile(r'(/^([0-2]?\d{0,2}\.){3}([0-2]?\d{0,2})$/)')
p = re.compile(r'(/\s[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1}\s/)')
a = re.findall(p,file)
print a
for i in a:
    print i
