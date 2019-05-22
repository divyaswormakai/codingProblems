# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0 n1
#   / \
#  1   0 n2 n3
#     / \
#    1   0 n4 n5
#   / \
#  1   1 n6 n7

class node:
	def __init__(self,val,par):
		self.value = val
		self.parent =par
n=[]
n1= node(0,None)
n2=node(1,n1)
n3=node(0,n1)
n4=node(1,n3)
n5=node(0,n3)
n6 =node(1,n4)
n7 = node(1,n4)
n.append(n1)
n.append(n2)
n.append(n3)
n.append(n4)
n.append(n5)
n.append(n6)
n.append(n7)
count=0

for i in range(len(n)-1,-1,-1):
	node = n[i]
	while(node.parent!=None):
		if(node.value==node.parent.value):
			count+=1
		else:
			break
		node=node.parent
print(count)
	
