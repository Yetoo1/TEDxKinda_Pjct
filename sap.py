#This is a test to see how to efficiently sort this shit so that the flights get on the graph the way the user wants
#starting simple with individual lists, going to make multidimensnional or something crap later 
flights = {"B6 21324", "WN 1826", "WN 1321", "KL 1234"} #one of them, KL 1234 isn't a real flight, since the aircode isn't real
times = {"6:30 pm", "4:21 am", "69:69 pm", "2:69 am"} #this will be converted to military time for easier math
def main():
	print flights,"\n", times	
	flights[0] = flightstocut[1:]
	#flightcut =  flightstocut[1:]
	print flightstocut 
main()
