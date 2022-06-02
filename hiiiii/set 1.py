
#1
t=int(input("enter the free space in bytes:"))
u=int(input("enter the used space:"))
a=t+u
o=int(input("Enter the size of deleted file:"))
n=u-o
h=int(input("Enter the size of new file:"))
m=n+h 
print("The free bytes in the memory =",a-m)

#3
f=open("mydata.txt","w")
f.write("name-ram  phone no-78945612  roll no-51  branch-cs")
f.close()
