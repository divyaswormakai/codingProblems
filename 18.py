# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you 
# do not need to store the results. You can simply print them out as you compute them.

arr=[]

while True:
	x=input("Enter a number:")
	try:
		x = int(x)
		arr.append(x)
	except ValueError:
		break
print("the input values are: ",arr)
k =int(input("enter the length of substring:"))
lengtho = k
start = 0
last = len(arr)

while(k<=last):
	temp = arr[start:k]
	temp.sort()
	print(temp[lengtho-1])
	start+=1
	k+=1

