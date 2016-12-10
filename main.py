#!/usr/bin/env/ python
#MIT License

#Copyright (c) 2016 Yetoo1, Scott Cohen

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#If you contributed to this file, add your name to the author variable and the credits variable, if you didn't contribute to this file, add your name to the credits variable
__author__ = "Scott Cohen"
__copyright__ = "Copyright 2016, Samirs Call"
__credits__ = "Scott Cohen"
__license__ = "MIT"
__version__ = "<need to make shell script to increment version and send to git>"
__maintainer__ = "Scott Cohen"
__email__ = "yetoohappy@gmail.com"
__status__ = "Development"  
#from HTMLParser import HTMLParser
import urllib2
import re
response = urllib2.urlopen('http://webservice.prodigiq.com/wfids/LGB/small?rows=20#qt-flights_small_view')
html = response.read()
html = html.split("\n")
#yes a better way would to be splitting the file up into two parts so you don't have to wait for the program to trip over itself, but I really don't want to at the moment, if someone else does plase implement it 
#for the gui, the table of values will show
#also, ask teacher for verification if this is going in the right direction
#make recommended to view 7 at once as the actual page changes count, wait crap, it doesn't matter just make it all some large number, like 35 so that it gets a list of all planes, but the user can still decide 

#what this code should hvae been doing is inputting individual words into a database referenced by a tag so it would be easier to find everything, but for the general prupose of this, what we have here, to the extent of my knowledge, is alright.
def arrivals():
	print "Arrivals\n"
#this little bit is only for the arrivals, the departures will come later
#I also don't even know how this is managing to work since there are <td> tags before the ones we need>
#This will break if the user sets a number too high as, the script will think that the data is coming from departures, so there needs to be a set stopping point. The only problem is that I'm having a hard time counting each on that happens, just to note, on the link above, the site shows 17 entries but the html file I downloaded separate from the html downloaded in the code has more than 17. Someone will eventually need to fix that by counting how much there are. WAIT I HAVE FOUND THE CLASS WHICH CONTAINS THIS BUT IT ENDS AT 19 IN CASE ANYONE WANTS TO KNOW
#also, as of now this is the console version, the final version will be gui	
	i = 0
	k = 0
	listamount = 19 #this variable will be changed by the user and will have a global varient just incase the user wants to see both the arrivals and departures by this interval. The maximum possibility of this variable for a unique result is 19 NO WAIT IT COULD BE 12? CRAP IT CHANGES!. The default could be 7 but it most likely will change. When global variable implemented, must create if statements to detect a switch that occurs when a button is pressed to use gloabl instead of local
	pattern = "<td>"
	pattern2 = "<div class=\"view view-departures"
	for line in html:
	     #for c in line:
		#print line
		#this is here to stop any possibility of going over to the next dataset
		if pattern2 in line:
			print "Reached the end of section!"					
			break		
		
		if pattern in line:
			#is just finding location
			#get the ontime part
			#the match and stuff isn't needed, it's kept for now just in case it actually is needed			
			match = re.search(pattern, line)
			s = match.start()
			linenospace = line.split("</td>", 1)[0]
			linenospace2 = linenospace.split("<td>", 1)[-1]	
			print linenospace2		
			i += 1
			#as of now it's modulo 4 but it should become five for a tag that it's not reading but soon will
			if i % 4 == 0:			#this is for debugging			
				print "-----",i/4,"-----"	#also this is part of the comment above	
			if i % 4 == 0 and i == listamount * 4: 
				#print "end" this won't work because this doesn't mean it won't stop iterating			
				print "Reached the end of the user's selection. of arrivals."			
				break
								
			#fix	
def departures():
	print "Departures:\n"				
	#i = 76 #doesn't matter if you set the i, it starts at the same place, remember we are sorting lines here, we are merely manipulating the mechanisim to sort through lines.
	i = 0
	k = 0
	verify = 0
	listamount = 19
	#start = "view-id-departures"
	pattern = "<td>"
	for line in html:
	#for i in range (76, len(html))	
		if pattern in line:			
			linenospace = line.split("</td>", 1)[0]
			linenospace2 = linenospace.split("<td>", 1)[-1]
			if i > 75:						
				print linenospace2
			i += 1
			if i % 4 == 0 and i > 76: #19 * 4
				#a = i - 76				
				print "-----",(i/4)-19,"d-----" # the d is for departure to differentiate from the detatched present which is is the arrivals (failed attempt at aliteration)
			#this is the proprietary, this is what we are manipulating, the if statement, we are chaning the amount of water that goes into the stream, the if statement is the log. Just changing the rate of the water will change it, i, it's the ultimate exit that changes it.  
			#if i % 4 == 0 and i == (listamount * 4)+76: #19 * 4
			if i % 4 == 0 and i == listamount * 4:			
				print "Reached the end of the user's selection of departures."		
				break
			
				

arrivals()
print "\n"
departures()	
	
#plane
#city
#time
#gate

