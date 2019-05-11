# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the 
# Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

a =[]

while True:
	x=input('Enter R/G/B:')
	if(x not in ['R','G','B','r','g','b']):
		break
	a.append(x)


if __name__ == "__main__":
	count =0
	for i in range(0,2):
		if(i==0):
			avail = ['R','r']
		if(i==1):
			avail = ['G','g']
		for j in range(count,len(a)):
			if(a[j] in avail):
				if(a[count] not in avail):
					temp = a[j]
					a[j] = a[count]
					a[count] = temp
				count+=1
	print(a)