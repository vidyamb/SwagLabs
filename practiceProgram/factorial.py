x = int(input("Enter a number to find factorial :"))
factorial = 1

if x < 0:
    print("sorry , negative value does not have factorial")
elif x == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, x + 1):
        factorial = factorial * i
print("Factorial of", x, "is", factorial)
