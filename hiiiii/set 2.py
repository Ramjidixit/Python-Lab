#1 
a=(275000*30*4*15)/100
g=a/4
b=g/30
c=int(input("Enter the number of months in which growth takes place: "))
d=c*30
print("Total number of passengers=",275000*365+d*b)