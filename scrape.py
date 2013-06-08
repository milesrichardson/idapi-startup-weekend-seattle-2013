#!/usr/bin/env python

import urllib, urllib2
import os
import argparse

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


def get_familywatchdog_results(firstname="John", lastname="Smith", statecode="CA"):
	payload = { 'txtLastName': lastname, 
				'txtFirstName': firstname,
				'txtState': statecode,}
	payload = urllib.urlencode(payload)

	response = urllib2.urlopen(url=familywatchdog_url, data=payload)
#print response.read()

	temp_filename = 'temp.html'
	curdir = os.path.realpath(os.curdir)
	f = open(os.path.join(curdir, temp_filename), 'w')
	response_body = response.read()
	f.write(response_body)
	f.close()

	NO_OFFENDERS = 'No offenders found.'

	#if 


	print os.path.join(curdir, temp_filename)


def main():
	parser = argparse.ArgumentParser(description='Get FamilyWatchDog Report')
	parser.add_argument('--firstname', '-first', nargs='?', const=1, help="First Name of Person" )
	parser.add_argument('--lastname', nargs='?', const=1, help="Last Name of Person" )
	parser.add_argument('--statecode', nargs='?', const=1, help="Two Character State Code" )
	args = parser.parse_args()

	get_familywatchdog_results(args.firstname, args.lastname, args.statecode)

if __name__=="__main__":
	main()
