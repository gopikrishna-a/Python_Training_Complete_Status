#Language---->Python 2.7
#Created by A.Gopikrishna on 11/01/2017

#Task-1

value = raw_input("Enter Value : ")
print value

#Task-2
#Tupples:A tuple is a sequence of immutable Python objects.

tup_value=("mon","tue","wed","thu","fri","sat","sun")
inp=raw_input("enter day number  :")
inp=int(inp)
print tup_value[inp]


#Task-3
#Lists:The list is a most versatile datatype in Python

list_month=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
month=raw_input("enter number :")
month=int(month)
end=month*3
start=end-3
print list_month[start:end]


#Task-4
#Dictonary:Each key is separated from its value by a colon (:)
month_dictonary={'jan':31,'feb':28,'mar':30,'apr':31,'may':30,'jun':31,'july':30,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
inp=raw_input("enter month name :")
inp=int(inp)
print month_dictonary['key']
for m in month_dictonary:
    print (month_dictonary)


#Task-5
#Using Inbuilt Functions
list_num=[1,2,3]
print max(list_num)
print main(list_num)

