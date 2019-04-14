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
