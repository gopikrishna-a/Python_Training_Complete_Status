
Created by A.Gopikrishna on 13/01/2017
#Language ---> Python 2.7.3

#task-1
#Using inbuilt functions
print "===List sorting==="
lists = [123, 'xyz', 'zara', 'abc', 'xyz']
print "Given list is  :",lists
lists.sort()
print "Sorted list is :",lists




#Task-2 Reversing a string
print "===Reverse of given input==="
def reverse( a ):
    return a[::-1]

a = (raw_input("Enter anything :"))
print "Reverse of given input is :",reverse(a)




#Task-3
print "===Reverse of Given List==="
def reverse(a):
    return a[::-1]

a = ["ASM" "Technologies" "ltd"]#using list
print a
print "reverse of given list is :",reverse(a)


#Task-4

#Lower case to Upper case and Upper case to lower text convertion
def change(a):
    
    print a.swapcase()
    return
    
a =  raw_input("enter input text:",raw_input("enter text :"))
change(a)














