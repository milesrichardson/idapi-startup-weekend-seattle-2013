#!/usr/bin/env python

import urllib, urllib2
import os

familywatchdog_url = "http://www.familywatchdog.us/ShowMap_Status.asp" # for map view
familywatchdog_url = "http://www.familywatchdog.us/ShowList.asp" # for map list view (not working)
familywatchdog_url = "http://www.familywatchdog.us/ShowNameList.asp" # for name list

# following are for map list
street = '2502 North Ave'
city = 'Odell'
statecode = 'NE'
zipcode = '68415'

# following are for name list
lastname = "Smith"
firstname = "John"
statecode = 'CA'

payload = { 'txtLastName': lastname, 
			'txtFirstName': firstname,
			'txtState': statecode,}
payload = urllib.urlencode(payload)

response = urllib2.urlopen(url=familywatchdog_url, data=payload)
#print response.read()

temp_filename = 'temp.html'
curdir = os.path.realpath(os.curdir)
f = open(os.path.join(curdir, temp_filename), 'w')
f.write(response.read())

print os.path.join(curdir, temp_filename)
f.close()
