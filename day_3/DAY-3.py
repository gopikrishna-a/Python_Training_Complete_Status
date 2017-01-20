#Written by A.Gopikrishna on 13/01/2017
#Language : Python 
#Task-1(a)
print "===Prime Numbers Without Definations==="
count = 0
a = int(raw_input("Enter starting number :"))
b = int(raw_input("Enter ending number :"))

for i in range(a,b +1):
    
    if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           count+=1
           print(i)
print "Total numr of Primes are :",count



#Task-1(b)
#Printing Prime Numbers by Defining funcrion
print "===Prime Numbers Witmething (an object) back to the call so you can use ith Definations==="
count = 0
def prime(x):
    if x >= 1:

        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

a=int(raw_input("enter starting num :"))	        
b=int(raw_input("enter ending num :"))

for i in range(a,b):
    if prime(i):
        count += 1
        print i

print "Total Prime nums are ",count





#Task-2
print "===Avg of Given list==="
lists = [1,2,3,4,5,6,7,8,9,10]
print "Given list is :"
print lists
listsum = sum(lists)
print "sum of given list is %d:"%listsum
length = len(lists)
print "Length of given list is %d:"%length
avg = float(listsum)/float(length)
print "avg of given list is %f :"%avg



#Task-3
print "===Upper to lower and Lower to upper==="
A = raw_input('type in something lowercase.')
B = raw_input('type in the same thing caps lock.')
print "lowercase converted into upper :",A.upper()
print "upper case converted into lower case :",B.lower()




#Task-4
#Using inbuilt functions
print "===List sorting==="
lists = [123, 'xyz', 'zara', 'abc', 'xyz']
print "Given list is  :",lists
lists.sort()
print "Sorted list is :",lists




#Task-5 Reversing a string
print "===Reverse of given input==="
def reverse( a ):
    return a[::-1]

a = (raw_input("Enter anything :"))
print "Reverse of given input is :",reverse(a)




#Task-6
print "===Reverse of Given List==="
def reverse(a):
    return a[::-1]

a = ["ASM" "Technologies" "ltd"]#using list
print a
print "reverse of given list is :",reverse(a)


#Task-7

#Lower case to Upper case and Upper case to lower text convertion
def change(a):
    
    print a.swapcase()
    return
    
a =  raw_input("enter input text:",raw_input("enter text :"))
change(a)














