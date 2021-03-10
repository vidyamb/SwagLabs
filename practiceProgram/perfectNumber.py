num = int(input("Enter number to check perfect or not:"))
sum = 0
i = 1
while i < num :
    if num%i==0:
        sum=sum+i

    i += 1
if sum==num:
    print("Perfect")
else:
    print("not perfect")




