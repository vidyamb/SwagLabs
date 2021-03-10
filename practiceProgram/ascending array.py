import array
import math

vidar = [5, 3, 8, 2, 1]
temp = 0
print("Original array is:")
for i in range(0, len(vidar)):
    print(vidar[i])

for i in range(0, len(vidar)):
    for j in range(i + 1, len(vidar)):
        if vidar[i] < vidar[j]:
            temp = vidar[i]
            vidar[i] = vidar[j]
            vidar[j] = temp
    print()

for i in range(0, len(vidar)):
    print(vidar[i])

x = math.factorial(2)
print(type(x))
print(x)

