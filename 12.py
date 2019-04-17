# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a 
# set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

step=input("Enter the number of steps::")

arr12=[]
arr135=[]
steps1=0
steps2=0

for i in range(0,int(step)):
	if(i==0):
		arr12.append(1)
	elif(i==1):
		arr12.append(2)
	else:
		arr12.append(arr12[i-1]+arr12[i-2])
	steps1 =arr12[i]

for i in range(0,int(step)):
	if(i==0):
		arr135.append(1)
	elif(i==1 or i==2):
		arr135.append(2)
	else:
		arr135.append(arr135[i-1]+arr135[i-2])
	steps2 =  arr135[i]

print("With 1 or 2 steps it will take",str(steps1),"steps")
print("With 1 or 3 or 5 steps it will take",str(steps2),"steps")

