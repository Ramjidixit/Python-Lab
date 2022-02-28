print("--------------distance between two points---------------------")
print("enter the value of first coordinates:")
a=int(input('enter x1:'))
b=int(input('enter y1:'))
print("enter the value of second coordinates:")
c=int(input('enter x2:'))
d=int(input('enter y2:'))
e=(((c-a)**2)+((d-b)**2))**0.5
print("the distance between two points is=%.2f "%e)
