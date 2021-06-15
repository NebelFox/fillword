import atexit
from time import time
start_time = time ()
print ("Starting time: {}".format (start_time))

def onexit ():
	endtime = time ()
	print ("Ending time: {}".format (endtime))
	print ("Elapsed time: {}".format (endtime-start_time))

atexit.register (onexit)