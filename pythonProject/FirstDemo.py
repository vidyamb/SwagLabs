print("hello")
a = 4
print(type(a))
print(a)
f, b, c = 5, 7.90, "great"
print(f, b, c)
#print("value is " + b)

print("{} {}".format("value is ", b))
d="VIDYA"
print(d+'lakshmi')
lst=[1,5.6,899.90,"apu"]
print(lst[0])
print(lst[1:])
lst.insert(2,'xyz')
print(lst)

#if else
madhu = "dummi"
a=9
if madhu=="dumm":
    print("madhu is dummy and moti")
else:
    print("madhu is loffer munde")
print("if else condition done")

def GreetMe(name):
    print("Gud morning" + name)

GreetMe("vidya")

def addintegers(a,b):
    return(a+b)

print(addintegers(2,4))

class Calculator:
    num=200

    def getData(self):
        print("i am method of the class")

    def __init__(self, a , b):
        self.firstnum=a
        self.secondnum=b
        print("i am a constructor called automatically when objects created")

    def summation(self):
        return self.firstnum + self.secondnum + Calculator.num

obj= Calculator(2,3)
obj.getData()
print(obj.summation())

print(obj.num)






