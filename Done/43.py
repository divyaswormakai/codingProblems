# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, 
# then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, 
# then it should throw an error or return null.
# Each method should run in constant time.

stk=[2,4,5,22,1,4]

def pop():
	if(top>=0):
		temp = stk[top]
		top-=1
		return temp
	else:
		return -1
	# return temp[a--]

def push(val):
	global top
	stk.append(val)
	top=top+1
 
def max():
	temp=stk
	temp.sort()
	return temp[len(temp)-1]

if __name__=="__main__":
	top=0
	print(max())

