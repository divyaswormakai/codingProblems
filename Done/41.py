# Given an unordered list of flights taken by someone, each represented as [origin, destination) pairs, and 
# a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are 
# multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
#  starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should 
# return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
# However, the first one is lexicographically smaller.

a = [['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']]
lists=[]
def findFlight(targ):
	for i in range(len(a)):
		if(targ == a[i][0]):
			lists.append(a[i][1])
			return findFlight(a[i][1])

if __name__=="__main__":
	target = 'HKO'
	lists.append(target)
	findFlight(target)
	print(lists)
