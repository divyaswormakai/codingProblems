import os

cwd = os.getcwd()

for i in range(0,55):
	filename = cwd + "\\"+str(i)+".py"
	open(filename,'w').close()