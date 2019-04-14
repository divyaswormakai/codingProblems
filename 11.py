# Implement an autocomplete system. That is, given a query string s and a set of all possible 
#query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

import re


dictionary =  ["dog","cat","mat","apple","deer","deal","deaf","reaf"]

inp= input("Enter the query string:")

for i in dictionary:
	res = re.search("^"+inp,i)
	if(res):
		print(i)
