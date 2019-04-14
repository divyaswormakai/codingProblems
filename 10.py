import time

def JobScheduler(printMsg,waitTime):
	waitTime = waitTime/1000
	printMsg()
	time.sleep(waitTime)

def printMsg():
	print("Done")

JobScheduler(printMsg)