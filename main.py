from HTMLParser import HTMLParser
import urllib2
import re
response = urllib2.urlopen('http://webservice.prodigiq.com/wfids/LGB/small?rows=20#qt-flights_small_view')
html = response.read()
html = html.split("\n")
#print html
#for line in html:
	#print line
	#if (line)
#for the gui, the table of values will show
#also, ask teacher for verification if this is going in the right direction
def arrivals():
#this little bit is only for the arrivals, the departures will come later
#I also don't even know how this is managing to work since there are <td> tags before the ones we need>
#This will break if the user sets a number too high as, the script will think that the data is coming from departures, so there needs to be a set stopping point. The only problem is that I'm having a hard time counting each on that happens, just to note, on the link above, the site shows 17 entries but the html file I downloaded separate from the html downloaded in the code has more than 17. Someone will eventually need to fix that by counting how much there are. WAIT I HAVE FOUND THE CLASS WHICH CONTAINS THIS BUT IT ENDS AT 19 IN CASE ANYONE WANTS TO KNOW
#also, as of now this is the console version, the final version will be gui	
	i = 0
	k = 0
	listamount = 7 #this variable will be changed by the user and will have a global varient just incase the user wants to see both the arrivals and departures by this interval. The maximum possibility of this variable for a unique result is 19. The default could be 7 but it most likely will change.
	pattern = "<td>"
	pattern2 = "<div class=\"view view-departures"
	for line in html:
	     #for c in line:
		#print line
		#this is here to stop any possibility of going over to the next dataset
		if pattern2 in line:
					print "huh"
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
				print "-----",i/4,"----"	#also this is part of the comment above	
			if i % 4 == 0 and i == listamount * 4: 
				#print "end" this won't work because this doesn't mean it won't stop iterating
				break
				#pass
				
	
		
arrivals()		
	
#tagb = 0
#tagba = 0

#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#	if tag == "!tr":	
#		tagb = 0
#	elif tag == "tr":        
#		print "Encountered a start tag:", tag
#		tagb = 1	
#	else:
#		tagb = 0 #just to be sure, like I know that the if not is already doing it's job, but still, I feel like some of these variables are tricky dicky
#      

#    def handle_endtag(self, tag):
#	if (tag != "tr"):
#		tagba = 0
#	elif tag == "tr":
#        	print "Encountered an end tag :", tag
#    		tagba = 1
#	else:    
#		tagba = 0

#     
#   
## instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
#parser.feed(html)

