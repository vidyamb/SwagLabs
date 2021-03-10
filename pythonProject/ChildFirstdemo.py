import self as self

from FirstDemo import Calculator

class ChildImpl(Calculator):
    num1 = 100

    def __init__(self):
        Calculator.__init__(self, 2, 9)

    def getcompletedata(self):
        return self.num + self.num1

obj=ChildImpl()
print(obj.getcompletedata())
#obj.Calculator(2 , 3)

str1="Vidyalakshmi shivanand shet"
str2="software TestEngineer"
str3="lakshmi"
str4=" Great "

print(str1[12])  #to print 12th place char
print(str1[0:8])  #to print substring 0 to 7
print(str3 in str1) #to check substring in another string
print(str2.split("E"))
print(str1 + str4)
print(str4.strip())
print(str4.rstrip())
print(str4.lstrip())

