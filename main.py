import urllib2
response = urllib2.urlopen('http://www.lgb.org/travelers/flight_status.asp')
html = response.read()
#print html
html = html.split("\n")
for line in html:
	print line
