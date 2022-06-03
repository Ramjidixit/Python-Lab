a=input()
b="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
c=0
for i in b:
    if i in a:
        c=c+1 
if c==26:
    print("pamgram ")
elif c>26:
    print("pangram ")
else:
    print("not pangram ")
