print("--------------compound interest---------------------")

p=int(input('enter principle amount:'))
r=int(input('enter rate:'))
t=eval(input('enter time period in year:'))
a=p*(pow((1+r/100),t))
print("the compound interest  is=%.2f "%a)
