#Cnnecting to MySql database
#Task-1
import MySQLdb

db = MySQLdb.connect("localhost","root","asm123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()



#Task-2
#Creating New table and including columns

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","asm123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS ACCESSPOINTS")


# Create table as per requirement
sql = """CREATE TABLE ACCESSPOINTS(
         MACAddress VARCHAR(255),
         IPv4Address VARCHAR(255),
         IPv6Address VARCHAR(255),
         Name VARCHAR(255),
         State VARCHAR(255),
         Tunnel VARCHAR(255),
         Sec_Mode VARCHAR(255),
         Mesh_Role VARCHAR(255),
         PSK VARCHAR(255),
         Timer VARCHAR(255),
         HW_Version VARCHAR(255),
         SW_Version VARCHAR(255),
         Model VARCHAR(255),
         Serial_number VARCHAR(255)
         );"""
cursor.execute(sql)
# disconnect from server
db.close()


#Task-3
#Extracting the Data Between Two Matching Strings i.e "APmgr info: apmgrinfo -a" and "65 APs are connected"
import MySQLdb

db = MySQLdb.connect("localhost","root","asm123","TESTDB" )
cursor = db.cursor()



#!/usr/bin/python
import re
import sys
import mysql.connector

#Opening the diag.out file
file=open("/home/asm/diag.out")
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

sql =""""select * from ACCESSPOINTS"""
print("database selected")

for ap in aps:
	print ap


#Extracting The Data

import re
#1-Extracting mac address-->ok
print "==========MAC=========="
file = open('/home/asm/diag.out','rb').read()
a = re.compile(r'(\s[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2})')
      
fmac = re.findall(a,file)

for i in fmac:
    
    print i

#2-Extracting ipv4 address-->ok

print "==========IPv4=========="
file = open('/home/asm/diag.out','rb').read()
b = re.compile(r'/\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]/')

fipv4 = re.findall(b,file)
for i in fipv4:
    print i

#3-Extracting ipv6 address-->ok

print "==========IPv6=========="

file = open('/home/asm/diag.out','rb').read()
c = re.compile(r'[A-Za-z0-9]{1,4}::[0-9]{1}')
       
fipv6 = re.findall(c,file)
print c
for i in fipv6:
    print i

#4-Extracting Name-->

print "==========Name=========="
file = open('/home/asm/diag.out','rb').read()

name = re.compile(r'\s*Name\s*:\s*(.*)')
fname = re.findall(name,file)

for a in fname:
	ssec = a.split(":")
	print ssec[0]


#5-Extracting State-->ok
print "==========State=========="
file = open('/home/asm/diag.out','rb').read()

state = re.compile(r'\s*State\s*:\s*(.*)')
fstate = re.findall(state,file)

for a in fstate:
	ssec = a.split("/")
	print ssec[0]



#6-Extracting Tunnel-->ok

print "==========Tunnel=========="
file = open('/home/asm/diag.out','rb').read()
tun = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')

ftunnel = re.findall(tun,file)

for a in ftunnel:
	ssec = a.split("/")
	print ssec[0]



#7-Extracting Sec_Mode--->ok
print "==========Sec Mode=========="

file = open('/home/asm/diag.out','rb').read()

mode = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
fsec = re.findall(mode,file)

for a in fsec:
	ssec = a.split("/")
	print ssec[1]


#8-Extracting Mesh_Role-->ok

print "==========Mesh Role=========="
le = open('/home/asm/diag.out','rb').read()

mesh = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
fmesh = re.findall(mesh,file)



for a in fmesh:
	ssec = a.split(":")
	print ssec[0]




#9-Extracting PSK-->ok

print "==========PSK=========="
file = open('/home/asm/diag.out','rb').read()

psk = re.compile(r'\s*PSK\s*:\s*(.*)')
fpsk = re.findall(psk,file)



for a in fpsk:
	ssec = a.split(":")
	print ssec[0]




#10-Extracting Timer--ok


print "==========Timer=========="

file = open('/home/asm/diag.out','rb').read()
time = re.compile(r'\s*Timer\s*:\s*(.*)')

ftimer = re.findall(time,file)

for a in ftimer:
	ssec = a.split(":")
	print ssec[0]


#11-Extracting HW_Version--> ok
print "==========HW Version=========="

file = open('/home/asm/diag.out','rb').read()

hw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
fhw = re.findall(hw,file)

for a in fhw:
	ssec = a.split("/")
	print ssec[0] 



#12-Extracting SW_Version-->ok

print "==========SW Version=========="
file = open('/home/asm/diag.out','rb').read()

sw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
fsw = re.findall(sw,file)

for a in fsw:
	ssec = a.split("/")
	print ssec[1] 




#13-Extracting Model--ok

print "==========Model=========="
file = open('/home/asm/diag.out','rb').read()
mdl = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')

fmodel = re.findall(mdl,file)

for a in fmodel:
	ssec = a.split("/")
	print ssec[0]



#14-Extracting Serial_Num-->ok

print "==========Serial Num=========="
file = open('/home/asm/diag.out','rb').read()

ser = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
fser = re.findall(ser,file)

for a in fser:
	z = a.split("/")
	print z[1]




if len(fmac)==len(fipv4)==len(fsw)==len(fhw)==len(fname)==len(fstate)==len(ftunnel)==len(fsec)==len(fmesh)==len(fpsk)==len(ftimer)==len(fmodel)==len(fser)==len(fipv6):
            for i in range(len(fmac)):
                        cursor.execute("""INSERT INTO ACCESSPOINTS(Name,MACAddress,IPV4Address,SW_Version,HW_Version,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,Model,Serial_number,IPv6Address)
                         VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % (fname[i],fmac[i],fipv4[i][1:-1],fsw[i][11:23],fhw[i],fstate[i],ftunnel[i],fsec[i][15:18],fmesh[i],fpsk[i],ftimer[i],fmodel[i],fser[i][9:21],fipv6[i]))

try:
    db.commit()
except:
    db.rollback()
    db.close()



