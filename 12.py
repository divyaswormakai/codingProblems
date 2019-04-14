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

