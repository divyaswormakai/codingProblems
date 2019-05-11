# Given a array of numbers representing the stock prices of a company in chronological order, 
# write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
# You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and 
# sell it at 10 dollars.

a=[9,11,4,5,7,16]
minInd=0
maxVal=0
for i in range(0,len(a)):
	if(a[i]<a[minInd]):
		minInd = i
	else:
		temp = a[i]-a[minInd]
		if(temp>maxVal):
			maxVal =temp

print(maxVal)

