num = int(input("enter number:"))
sum = 0
temp = num
n = len(str(num))
print(n)
print(temp)
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print("this is armstrong number")

else:
    print("Not")
