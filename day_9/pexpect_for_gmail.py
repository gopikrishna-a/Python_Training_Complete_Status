#Created By A.Gopikrishna On 23/01/2017

#What is Pexpect:-
#Pexpect is a pure Python module that makes Python a better tool for controlling and automating other programs.
#Example code on pexpect module.
#Sending G-Mail Using Pexpect Code

import pexpect
import sys
m = pexpect.spawn('python gmail_sample.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline('')#enter receiver mail id here
m.expect("Password:")
m.sendline('')#enter ur password here
m.expect("To address :")
m.sendline(" ")##enter receiver mail id here
m.expect("Subject :")
m.sendline("Test")#Enter subject here
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")#Enater ur mail body content here
m.sendline("end")
m.expect("test has been send to a.gopikrishna@gmail.com")
m.close()


