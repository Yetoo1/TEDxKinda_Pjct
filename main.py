import urllib2
response =urllib2.urlopen('http://www.lgb.org/travelers/flight_status.asp')
html = repsponse.read()
#print html
