
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

compound_interest = p*(1+r/100)**t
print("The compound interest is", compound_interest)


