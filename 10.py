# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def JobScheduler(printMsg,waitTime):
	waitTime = waitTime/1000
	printMsg()
	time.sleep(waitTime)
	JobScheduler(printMsg,5000)

def printMsg():
	print("Done")

JobScheduler(printMsg,5000)

