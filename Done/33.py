# Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
# print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
numbers =[2,1,5,7,2,0,5]
med =0
for i in range(0,len(numbers)):
	tempNum = numbers[0:i+1]
	tempNum.sort()
	if(len(tempNum)%2==1):     #odd
		mid = len(tempNum)//2
		print(tempNum[mid])
	else:	#even
		mid = len(tempNum)//2
		midVal =(tempNum[mid-1]+tempNum[mid])/2
		print(midVal)
