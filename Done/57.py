# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
# You must break it up so that words don't break across lines. Each line has to have the maximum possible amount 
# of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between 
# each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
# you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in 
# the list has a length of more than 10.

string = "the quick brown fox jumps over the lazy dog"
k=10
i=0


while i<len(string):
	temp=""
	if (i+k) <len(string):
		if (string[i+k+1].isspace()):
			i=i+k+1
			for a in range(i-k,i):
				temp+=string[a]
		else:
			for j in range(i+k,i,-1):
				if(string[j].isspace()):
					for a in range(i,j):
						temp+=string[a]
					i=j
					break
		
	else:
		for a in range(i,len(string)):
			temp+=string[a]
		i=len(string)
	print(temp)


