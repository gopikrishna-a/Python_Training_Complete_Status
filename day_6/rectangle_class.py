class Rectangle:
 count = 0
 def __init__(self,x,y) :
   self.length=x
   self.width=y
   Rectangle.count=Rectangle.count+1
 def __str__(self):
    return 'Rectangle({0},{1})'.format(self.length,self.width)
 def __add__(self,other):
    return Rectangle(self.length+other.length,self.width+other.width)
 def __eq__(self,other):
    return Rectangle(self.length==other.length,self.width==other.width)
 def area(self):
    return self.length * self.width
 def perimeter(self):
    return 2 * self.length
 def issquare(self):
    if self.length == self.width:
     return True
 @staticmethod
 def getcount():
   return Rectangle.count
R=Rectangle(2,2)
print R
a=R.area()
print "Area:",a
b=R.perimeter()
print "Perimeter:",b
if R.issquare():
   print "Square"
else:
   print "Not Square"
R1=Rectangle(2,3)
R2=Rectangle(2,4)
R3=R1+R2
print "R3:",R3
a=R3.area()
print "Area:",a
if R1 == R2:
  print "same:"
else:
  print "NotSame:"
d=Rectangle.getcount()
print "Count :",d
