# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found 
# in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. 
# Similarly, given the target word 'MASS', you should return true, since it's the last row.

a = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]
target="FOAM"
target2 = "MASS"

for j in range(len(a[0])):
	temp=""
	for i in range(len(a)):
		temp+=a[j][i]
	if(target == temp):
		print(target,"is in the ",i+1,"row")
	if(target2 == temp):
		print(target2,"is in the ",i+1,"row")

for j in range(len(a)):
	temp=""
	for i in range(len(a[0])):
		temp+=a[i][j]
	if(target == temp):
		print(target,"is in the ",j+1,"column")
	if(target2 == temp):
		print(target2,"is in the ",j+1,"column")

