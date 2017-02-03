
import MySQLdb
import sys
import smtplib
import getpass
connection = MySQLdb.connect("localhost","root","asm123","TESTDB" )

cursor = connection.cursor ()

cursor.execute ("select ID,Name,Age from Students")

# fetch all of the rows from the query
mes = cursor.fetchall ()
string=''
for row in mes:
	line="%s\t %s\t %s"%(row[0],row[1],row[2])
	string=string+line+'\n'
print string


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
message = "subject:  %s\n%s"%(sub,string)

server.sendmail(username,to,message)
cursor.close ()
connection.close ()
