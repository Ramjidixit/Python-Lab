""". Program to input the number of overs in a Cricket match and output the maximum runs a
	player can score in the match. Assume that there are no extra runs or NO balls in the match
	played. For example, in a 50 over match, the maximum runs scored are 1653."""
	
a=int(input("enter the number of overs:"))

x=((a-1)*33)+36
print("the maximum runs a player can score in the match=",x)
