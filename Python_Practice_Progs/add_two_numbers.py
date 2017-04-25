#Type-1
class addition():
    def function(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print c

add=addition()
add.function(2,3)


#Type-2
class addition():
    def function(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print c

aa=addition()
a=int(raw_input("Enter first Number\n"))
b=int(raw_input("Enter Second Number\n"))
aa.function(a,b)
