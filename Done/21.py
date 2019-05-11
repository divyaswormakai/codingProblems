arr=[]
count =0
while True:
	print("-------------")
	x=input("Enter a start time:")
	y=input("Enter an end time:")
	try:
		x = int(x)
		y = int(y)
		temp=[x,y]
		arr.append(temp)
	except ValueError:
		break

for i in range(0,len(arr)-1):
	val = arr[i]
	start = val[0]
	endT = val[1]
	for j in range(i+1,len(arr)):
		newVal = arr[j]
		newStart =newVal[0]
		newEnd=newVal[1]
		print(newStart,newEnd,"v/s",start,endT)
		if(start>newStart and start<newEnd):
			count+=1
			print("found")
		elif(endT<newEnd and endT>newStart):
			count+=1
			print("found")
		elif(newStart>start and newEnd<endT):
			count+=1
			print("found")
		else:
			continue

print("no of classes required is:",count)
