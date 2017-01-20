
#Created by A.Gopikrishna on 16/01/2017
#Language ---> Python 2.7
#File Operations

import sys

def main():
  print "Hello World"

if __name__ == "__main__":
  main()



#opening a file in read mode
f = open("new.txt", "r")
print "Name of the file: ", f.name
print "Opening mode : ", f.mode

#opening a file in write mode
f = open("new.txt", "w")
print "Name of the file: ", f.name
print "Opening mode : ", f.mode


#closing a file
f.close()

# Opening file and writing into file
f = open("new.txt", "wb")
f.write( "hi.\nHello World!!\n");
f.close()



import sys

def main():
  print sys.argv

if __name__ == "__main__":
  main()

# Deleteting file
import os

os.remove("new.txt")


#creating a new directory
import os

os.mkdir("hello")

#getting the current working directory
import os

os.getcwd()


#Remove directory
import os

os.rmdir( "/asm/hello"  )










