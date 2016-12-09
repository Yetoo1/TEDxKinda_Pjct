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
pattern = "<tbody>"
for line in html:
     #for c in line:
	#print line
	if "<tbody>" in line:
		#print "found"
		match = re.search(pattern, line)
		s = match.start()
		print s
		break
	
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

