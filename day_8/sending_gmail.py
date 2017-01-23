#Created By A.Gopikrishna on 19/01/2017
#Language --> Python 2.7
#Sending Mail from Command Line Through Python Code

import smtplib
import getpass
import sys
host = "smtp.gmail.com"
port = 587
server =smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username = raw_input("Enter Ur Mail Id :")
v1=sys.argv[1]#Receiver Email Id
v2=sys.argv[2]#Attachment File Name
v3=sys.argv[3]#Subject
password=getpass.getpass("Enter Ur Password :")
server.login(username,password)
to =v1
sub =v3

file =open(v2,'r')
mes = file.read()
message = "subject:  %s\n%s"%(sub,mes)
server.sendmail(username,to,message)

#NOTE
#type below command in command line
#python running.py a.gopikrishna01@gmail.com git.txt hii



