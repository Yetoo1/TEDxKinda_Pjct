#this will download https://en.wikipedia.org/wiki/List_of_airline_codes and make it easier to put into a table, this program is merely temporary 
import urllib2
import re
response = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_airline_codes')
html = response.read()
html = html.split("\n")
def main():
	print "Reading tags"
	for line in html:
		if "<td>" in html:
			print line
		else:
			pass
main()
