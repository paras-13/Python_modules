from math import radians,sin,cos,tan,asin,acos,atan

# Trignometric functions and inverse trignometric functions
n5 = int(input("Enter a degree"))
        # Converting degree to radians as trignometric function accepts values in radian
n5 = radians(n5)       
Sin = sin(n5)
Cos = cos(n5)
Tan =tan(n5)
print("Trigbometric",Sin,Cos,Tan,sep="\n")

n2 = float(input("Enter number to find out its inverse "))
Isin = asin(n2)                 # Inverse functions provides output in radians
Icos = acos(n2)
Itan = atan(n2)
print("Inverse trignometric",Isin,Icos,Itan,sep="\n")