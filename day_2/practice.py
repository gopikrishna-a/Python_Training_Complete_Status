#created By A.gopikrishna on 12/01/2017

#Task--1

#Dictonarys
mydict = {'name':'gopikrishna','company':'ASM Technologies','role':'SE','age':22}

#To get contents of Dictonary
print mydict.items()
print mydict
print len(mydict)#length of Dictonary
print "\n"
#to add new item to Dictonary
mydict ['Loc']='Banglore'
print mydict.items()
print len(mydict)
print "\n"
#Updating an Item in Dictonary
mydict ['age']=23
print mydict.items()
print len(mydict)
print "\n"
#Deleting the Item from Dictonary
del mydict['age']
print mydict.items()
print len(mydict)
print "\n"
#To clear the entire Dictonary
mydict.clear()
print mydict.items()
print len(mydict)


#Task--2
lists = ["a","b","c","[1,2,3,4]","e","f"]
print lists
print len(lists)
print lists[0]
print lists[3]
print lists[3:2]

#TUPPLE(IMMUTABLE)
TUP=(1,2,3,4,5,6,7)
print len(tup)
print tup[0]

#Task-3
#Pattern Prog
for n in range(0,5):
    n +=1
    print ("*"*n) +" "

#Opening file and Reading data and closing it

file = open("new.txt", "r")

for line in file:
    print(line)

file.close() 

#More on tuples,lists and dictonarys
#Tuple

tup_value=("mon","tue","wed","thu","fri","sat","sun")
inp=raw_input("enter day number  :")
inp=int(inp)
print tup_value[inp]

#Lists

list_month=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
month=raw_input("enter number :")
month=int(month)
end=month*3
start=end-3
print list_month[start:end]

#Dictonary

month_dictonary={'jan':31,'feb':28,'mar':30,'apr':31,'may':30,'jun':31,'july':30,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
inp=raw_input("enter month name :")
inp=int(inp)
print month_dictonary['key']
for m in month_dictonary:
    print (month_dictonary)

