#1.
D ={'first':'this is first value','second’:"This is second value","GLa":"GLA University,Mathura" }
d1=dict((k.upper(), v) for k,v in d.items())
print(d1)

#2
"""THERE IS A FILE NAME data.txt that stores approx 20 lines .write a program to create a file name updated.txt
that stores only odd numbers of line"""
f=open("data.txt","r")
g=open("updated.txt","w")
cont=f.readlines()
for i in range(0,len(cont)):
    if(i%2!=0):
        g.write(cont[i])
    else:
        pass
f.close()
g.close()