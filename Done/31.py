# The edit distance between two strings refers to the minimum number of character insertions, deletions, 
# and substitutions required to change one string to the other. For example, the edit distance between “kitten”
#  and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

str1 = "kitten"
str2 = "sittings"
minLen = len(str1)
count= 0

if(len(str1)>len(str2)):
	minLen = len(str2)
	count = len(str1)-minLen

elif(len(str1)<len(str2)):
	minLen = len(str1)
	count = len(str2)-minLen

for i in range(0,minLen):
	if(str1[i] == str2[i]):
		continue
	count+=1

print(count)