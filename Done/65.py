# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

a= [[1,  2,  3,  4,  5],[6,  7,  8,  9,  10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]]

size = pow(len(a[0]),2)
# initial standard
curX=curY=0
minX=0
minY=0
maxX=len(a)
maxY=len(a[0])

while size>=0:
	# right movement
	while(curY<maxY):
		print(a[curX][curY])
		curY+=1
		size-=1
	curY-=1
	curX+=1
	minX+=1
	# down movement 
	while(curX<maxX):
		print(a[curX][curY])
		curX+=1
		size-=1
	curX-=1
	curY-=1
	maxY-=1
	# left movement
	while(curY>=minY):
		print(a[curX][curY])
		curY-=1
		size-=1
	curX-=1
	curY+=1
	maxX-=1
	# up movement
	while(curX>=minX):
		print(a[curX][curY])
		curX-=1
		size-=1
	curY+=1
	curX+=1
	minY+=1

