import random
import time

water_sprinkler=False
option=[True,False]
door=random.choice(option)
windows=random.choice(option)

def timer(n):
	print "Timer set for "+str(n)+" Minutes."
	print "Please Evacuate!"
	windows=True
	door=True
	
	while n>0:
		n=n-1
		if(n==0):
			water_sprinkler=True
			break
				

print "This is a trial Simulation of a Smoke Detector"
while 1:
	ppm=random.randint(1,500t)
	print ppm
	if ppm<70:
		water_sprinkler=False
		continue
	elif ppm>=70 and ppm<150:
		timer(60)
		break
	elif ppm>=150 and ppm<400:
		timer(10)	
		break
	else:
		timer(4)
		break



