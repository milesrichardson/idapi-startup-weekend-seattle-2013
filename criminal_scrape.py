#!../bin/python

import urllib, urllib2
import os
import argparse
import uuid
import time
import json
import string

source_filename = '../jailbase-sources.txt'
jailbase_url = "http://www.jailbase.com/api/1/search/"

if os.name=="posix":
	HIGHLIGHT_COLOR = '\x1b[96;1m'
	HIGHLIGHT_END = '\x1b[0m'
else:
	HIGHLIGHT_COLOR = ''
	HIGHLIGHT_END = ''

def get_jailbase_sources():
	fp = open(source_filename, 'r')
	sources = fp.read().split(' \n')
	fp.close()
	
	return sources

def get_results(firstname="", lastname="", source="nj-ecdc"):
	"""Requires no more than 1 request per second"""
	jailbase_url = "http://www.jailbase.com/api/1/search/"
	sources = get_jailbase_sources()

	if source=="all":
		print "Searching all", len(sources), "sources. Pausing 1 sec"
		time.sleep(1.1) 	# pause a tiny bit more than 1 sec between requests
		print "Not supported yet"
		return

	payload = { 'last_name': lastname, \
				'first_name': firstname, \
				'source_id': source }
	payload = urllib.urlencode(payload)

	if not firstname and not lastname:
		firstname = "John"
		lastname = "Smith"

	fullname = ""
	if lastname:
		lastname = lastname.upper()
		fullname = lastname
	if firstname: 
		firstname = firstname.upper()
		if not lastname:
			fullname += firstname
		else:
			fullname += ", " + firstname

	print "Searching criminal records for", colorify(fullname), "from", colorify(source)
	
	jailbase_url += "?" + payload
	print "Loading", jailbase_url
	req = urllib2.Request(url=jailbase_url)
	r = urllib2.urlopen(req)
	data = r.read()
	#data = json.load(r)
	return '\n' + data

def colorify(txt):
	return HIGHLIGHT_COLOR + txt + HIGHLIGHT_END

def main():
	parser = argparse.ArgumentParser(description='Get Criminal Records')
	parser.add_argument('--firstname', '-first', nargs='?', const=1, help="First Name of Person" )
	parser.add_argument('--lastname', '-last', nargs='?', const=1, help="Last Name of Person" )
	parser.add_argument('--searchall', '-searchall', nargs='?', const=1, help="Search all sources (max of 1 request per second)" )
	args = parser.parse_args()

	if args.firstname and args.lastname:
		print get_results(firstname=args.firstname, lastname=args.lastname)
	elif args.firstname:
		print get_results(firstname=args.firstname)
	elif args.lastname:
		print get_results(lastname=args.lastname)
	else:
		print get_results(firstname="John", lastname="Smith")


if __name__=="__main__":
	main()
