#This is a test to see how to efficiently sort this shit so that the flights get on the graph the way the user wants
from itertools import groupby
#starting simple with individual lists, going to make multidimensnional or something crap later 
flights = ["B6 21324", "WN 1826", "WN 1321", "KL 1234", "KL 3211", "L2 213"] #one of them, KL 1234 isn't a real flight, since the aircode isn't real
times = ["6:30 pm", "6:21 am", "69:69 pm", "2:69 am", "7:00 pm"] #this will be converted to military time for easier math
#these next two lists are for the flight function
#yes I could make it so that, since the way I'm doing it where optionsleft and optionsright have to be evaluated one at a time, that the two variables below could clear out everything and start appending for the next one, but like, I don't want to do that right now. I'll do it if the amount of lists grow very large and hard to manage, but wait, this paragraph might be void because the items don't both work the same way when trying to make a graph out of them.  
flightssmall = [] #this is where the cut flights are going to go
flightcount = [] #what the main program is going to look for when it is trying to find a ratio
timessmall = [] #this is hwere the cut time is going to go
#these next two lists are for the time function
timerange = ["6:30 pm", "7:00 pm"] #the program will convert from regular to military
flightg = 0
timeg = 0
def flight():
	#this is going to return a number for the same amount of flights portion of a ratio
	#this is kind of broken, since in this test we don't care which flight, but how much of each duplicate flight. Fix that, but make it a feature.
	#print flights,"\n", times
	
	#flightstocut = flights[0]
	#flightcut =  flightstocut[:2]
	#I'm tired so shut up about how convoluted this is
	#i = 0
	#k = 0
	#c = 0
	for index, item in enumerate(flights):
    		flightscut = flights[index].split(" ", 1)[0]
		flightssmall.append(flightscut)
		#print flightssmall
		b =[len(list(group)) for key, group in groupby(flightssmall)]	
		#print b
		if b[len(b) - 1] > 1:
			#print "asdas"
			flightcount.append(flightscut)
			#print flightcount		
	#	if flightscut in flightssmall:
	#		k += 1
	#		
	#	i =+ 1
	#for index2, item2 in enumerate(flightssmall):
	#	if flightscut in flightsmall[k]:
	#		c += 1	
	#print k
	return len(flightcount)
#############THIS IS THE DEVIATING LINE BETWEEN FLIGHT AND TIME, IT'S HOLY TOO!#########################################################
def time():
	for index, item1 in enumerate(timerange):
		a = timerange[index]
		#if a[len(timerange)-2:len(timerange)] == "am":
			#print "am"
		#	return "am"
		if a[len(timerange)-2:len(timerange)] == "pm":
			#print "pm"
			return "pm"
	#for index, item2 in enumerate(times):
		    		
		#times[index] = times2
		#times2 = times2[len(times)-2:len(times)]
		#timessmall.append(times2)
		#a = len(timessmall) #gets the length so that later when the thing counts, it increments 
		#for index, item2 in enumerate(timessmall)
		#	i += 1
		#	i.append(timessmall)		
		#b =[len(list(group)) for key, group in groupby(timessmall)]	
		#print b
		#if b[len(b) - 1] > 1:
			#print "asdas"
		#	flightcount.append(flightscut)
			#print flightcount		
	#	if flightscut in flightssmall:
	#		k += 1
	#		
	#	i =+ 1
	#for index2, item2 in enumerate(flightssmall):
	#	if flightscut in flightsmall[k]:
	#		c += 1	
	#print k	

options = raw_input("Enter the ratio. (0 is flights, 1 is time) Example: 0 1 is equivalent to flights over time ")
optionsleft = options[0]
optionsright = options[2]
#print optionsleft, "\n", optionsright
#I wanted to do a dictionary as a case statement but tobad, that's too hard at the moment.
optionsleft = int(optionsleft)
optionsright = int(optionsright)
#this won't work as it won't print a ratio, make it print a ratio
if optionsleft == 0 or optionsright == 0:
	print flight()
	flightg = flight()
if optionsleft == 1 or optionsright == 1:
#the time needs to be polished, since there is a lot of possible times with all those minutes and such, so I need to make it so that the user can pick wich range of times to choose from, in this test, we are assuming the range is from 6:00 pm to 7:00 pm, remember the time of day is very important. Also, the scope of the data that is going to be displayed could be what is the average time in general. Add feature where you could input a plane identification and it would find the time for that, but for now it's all about identification
	print time()
	timeg = time()

