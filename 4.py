# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

arr =[]
while True:
	x=input('Input a number')
	try:
		x = int(x)
		arr.append(x)
	except ValueError:
		break
print(arr)

for var in arr:
	if(var<0):
		arr.remove(var)

length = len(arr)-1
arr.sort()
print(arr)

if(arr[0]!=0):
	print("the lowest number is 0")
else:
	for i in range(0,length):
		if(arr[i+1]-arr[i]>1):
			print('The lowest number is' +str(arr[i]+1))
			break
