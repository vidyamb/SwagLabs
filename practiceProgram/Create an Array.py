from array import *
from operator import index

arr = array('i', [])

x = int(input("Enter the size of an array:"))

for i in range(x):
    y = int(input("Enter next element:"))
    arr.append(y)
print(arr)

var=int(input("enter element to search"))
g=0
for i in arr:
    if i == arr:
        pass
print(arr.index(var))
