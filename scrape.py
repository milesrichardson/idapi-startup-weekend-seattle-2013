#!/usr/bin/env python

import urllib, urllib2
import os

familywatchdog_url = "http://www.familywatchdog.us/ShowMap_Status.asp"
#familywatchdog_url = "http://www.familywatchdog.us/ShowList.asp"

street = '2502 North Ave'
city = 'Odell'
statecode = 'NE'
zipcode = '68415'


payload = { 'txtZipCode': zipcode, 
			'txtWidth': '',
			'txtStreet1': street,
			'txtState': statecode,
			'txtBrowser': 'Y'}
payload = urllib.urlencode(payload)

response = urllib2.urlopen(url=familywatchdog_url, data=payload)
#print response.read()

temp_filename = 'temp.html'
curdir = os.path.realpath(os.curdir)
f = open(os.path.join(curdir, temp_filename), 'w')
f.write(response.read())

print os.path.join(curdir, temp_filename)
f.close()
