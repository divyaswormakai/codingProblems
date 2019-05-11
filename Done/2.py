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


