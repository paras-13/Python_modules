# Exponential and Logarithmic functions in python
import math as m

# Square root
s_root = m.sqrt(int(input("Enter a number whose square root you want to find out")))
print(s_root)

# Return x raised to the power y
x,y = int(input("Enter a number")),int(input("You want to riase it by"))
Pow = m.pow(x,y)
print(Pow)

#Return e raised to the power x
epow = m.exp(int(input("Enter a number")))
print(epow)

# Logarithmic functions
num = int(input("Enter a number"))  
a = int(input("Base value"))  
print(m.log(x))             # For base e
print(m.log(num,a))         # For desired base
print(m.log10(num))         # For base 10

