

#Connecting To MySQldb 
import MySQLdb

db = MySQLdb.connect("localhost","root","asm123","TESTDB" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s " % data)

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS Students")


# Create table as per requirement
sql = """CREATE TABLE Students(
  ID varchar(30) NOT NULL,
  Name varchar(30) NOT NULL,
  Course varchar(40) NOT NULL,
  Branch varchar(40) NOT NULL,
  Age varchar(30) NOT NULL,
  City varchar(20) NOT NULL,
  Grade varchar(12) NOT NULL
);"""
cursor.execute(sql)


# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO Students (ID,Name,Course,Branch,Age,City,Grade)
         VALUES ('001','Ramu','B.tech','ECE','22','Banglore','A'),
('002','Seetha','B.tech','CSE','21','Hyderabad','A'),
('003','Dilip','B.tech','MECH','23','Banglore','A'),
('004','Raju','B.tech','CSE','21','Hyderabad','A'),
('005','Lakshman','B.tech','CSE','21','Hyderabad','A'),
('006','Smitha','B.tech','CSE','21','Vijayawada','A');"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()


import MySQLdb
import sys
import smtplib
import getpass
connection = MySQLdb.connect("localhost","root","asm123","TESTDB" )

cursor = connection.cursor ()

cursor.execute ("select ID,Name,Age from Students")

# fetch all of the rows from the query
mes = cursor.fetchall ()

mes1 = []
mes2 = []
mes3 = []

# print the rows
for row in mes:
	a = row[0],row[1],row[2]
	print a
	mes1.append(row[0])
	mes2.append(row[1])
	mes3.append(row[2])
print mes
for i in mes:
	print i	
#print ', '.join(mes1)
#print ', '.join(mes2)
#print ', '.join(mes3)
mess ='\t'.join(mes1) +"\n"+'\t'.join(mes2)+"\n"+'\t'.join(mes3)

print mess

#Sending Mail

host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username = raw_input("Enter Ur gmail ID :")
password=getpass.getpass()
server.login(username,password)
to = raw_input("Enter Receiver Email ID :")
sub = raw_input("Enter Subject of mail :")
message = "subject:  %s\n%s"%(sub,mess)

server.sendmail(username,to,message)
cursor.close ()
connection.close ()





