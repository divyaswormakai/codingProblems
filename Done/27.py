from array import *
import re

counter=0
stack = []

if __name__=="__main__":
	while True:
		x=input("string:: ")
		if(x=="a"):
			break
		else:
			if(counter == 0):
				stack.append(x)
				counter+=1
			else:
				for i in range(counter-1,-1,-1):
					if(stack[i]=="{" and x=="}"):
						stack.pop(i)
						counter-=1
						break
					elif(stack[i]=="[" and x=="]"):
						stack.pop(i)
						counter-=1
						break
					elif(stack[i]=="(" and x==")"):
						stack.pop(i)
						counter-=1
						break
					else:
						if(i==0):
							stack.append(x)
							counter+=1
							break
						else:
							continue

	if(counter ==0):
		print("True")
	else:
		print("False")


