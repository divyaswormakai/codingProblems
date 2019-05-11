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

