# Given an array of integers, return a new array such that each element at index i of the new array is
# the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

a=[]
b=[]
prod =1
while 1:
	x= input("input a number")
	if(x.isdigit()):
		a.append(int(x))
		prod =prod*int(x)
	else:
		break

# a = list(map(int,input().split(' ')))  -----for direct array input but have to use space for reasons
# method 1
# for var in a:
# 	temp = prod/var
# 	b.append(temp)

# method 2

for var in a:
	result =0
	temp = var + prod
	while(temp>var):
		temp = temp - var
		result+=1
	b.append(result)

print(b)


