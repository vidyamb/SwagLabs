# def Calc_comp_int(p, r, t):
#  amount = p * (pow((1 + r / 100), t))
# CI=amount-p
# print("CI is", CI)


# Calc_comp_int(5000, 2, 12)
principal = int(input("Enter principal amount:"))
rateOfInterest = int(input("Enter rate of interest :"))
Time = int(input("Enter time:"))
amount = principal * (pow((1 + rateOfInterest / 100), Time))
CI = amount-principal
print("Compound Interest is:", CI)
