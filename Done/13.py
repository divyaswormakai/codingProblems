# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

s="abcacba"
k=2
maxString=""

for i in range(len(s)):
	count=0
	chars=""
	chars+=s[i]
	kcount=1
	count+=1
	tempMaxString=""
	# get k no of distinct chars
	for j in range(i+1,len(s)):
		if(len(chars)<k):
			if(s[j]!=chars[kcount-1]):
				chars+=s[j]
				count+=1
		else:
			break
	tempMaxString=chars
	for l in range(j,len(s)):
		if(j==len(s)-1):
			break
		if s[l] in chars:
			tempMaxString+=s[l]
			count+=1
		else:
			break
	
	if(len(tempMaxString)>len(maxString)):
		maxString=tempMaxString

print(maxString)