#Write a C program to input all sides of a triangle and check whether triangle is valid or not. 

x=int(input("enter the smallest side of triangle:"))
y=int(input("enter the another side of triangle:"))
z=int(input("enter the largest side of triangle:"))
if(z<=x+y):
        print("triangle is valid")
else:
        print("triangle is not valid")
