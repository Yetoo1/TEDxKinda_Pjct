#This is a test to see how to efficiently sort this shit so that the flights get on the graph the way the user wants
#starting simple with individual lists, going to make multidimensnional or something crap later 
flights = ["B6 21324", "WN 1826", "WN 1321", "KL 1234"] #one of them, KL 1234 isn't a real flight, since the aircode isn't real
times = ["6:30 pm", "4:21 am", "69:69 pm", "2:69 am"] #this will be converted to military time for easier math
flightssmall = []
def main():
	print flights,"\n", times	
	#flightstocut = flights[0]
	#flightcut =  flightstocut[:2]
	i = 0
	k = 0
	for index, item in enumerate(flights):
    		flightscut = flights[index].split(" ", 1)[0]
		flightssmall.append(flightscut)
		print flightssmall
		if len(flightssmall) != len(set(flightssmall)):
			
			k += 1
		i =+ 1
	print k		 
main()

