# Calculating mean, mode and medain using python statistical module
import statistics as stat

print()
lst = eval(input("Enter a list of elements for which you want to find out mean -->"))
Mean = stat.mean(lst)             # To calculate mean
print("Mean of the given list of elements is-->",Mean)

print()
lst2 = eval(input("Enter a list of elements for which you want to find out mode -->"))
Mode = stat.mode(lst2)            # To calculate mode
print("Mode of the given list of elements is -->",Mode)

print()
lst3 = eval(input("Enter a list of elements for which you want to find out median -->"))
Median = stat.median(lst3)        # To calculate median
print("Median of the given list of elements is -->",Median)