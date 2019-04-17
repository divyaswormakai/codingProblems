# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits 
# and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

a=input("Enter the string:")
stringOP =""
count=0
temp=-1
i=0
while(i<len(a)):
	if temp == -1:
		temp=a[i]
		count=1
		i+=1
		continue
	else:
		if(a[i]==temp):
			count+=1
			i+=1
		else:
			stringOP+=str(count)+str(temp)
			# print(stringOP)
			temp=-1
			count=0
print(stringOP + str(count)+str(temp))





