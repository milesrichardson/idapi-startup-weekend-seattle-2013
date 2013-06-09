#!../bin/python

import urllib, urllib2
import os
import argparse
import uuid
import time
import json
import string

source_filename = 'jailbase-sources.txt'
jailbase_url = "http://www.jailbase.com/api/1/search/"

RECORDS_FILENAME = os.getcwd() + '/records.txt'
DBG = False

if os.name=="posix":
	HIGHLIGHT_COLOR = '\x1b[96;1m'
	HIGHLIGHT_END = '\x1b[0m'
else:
	HIGHLIGHT_COLOR = ''
	HIGHLIGHT_END = ''

def get_jailbase_sources(outputall=False):
	fp = open(source_filename, 'r')
	sources = fp.read().split(' \n')
	fp.close()
	
	if outputall:
		print sources

	return sources

def store_results(filename, results):
	f = open(filename, 'w')
	if DBG: print "Writing to", filename
	f.write(results)
	f.close()
	
def get_stored_results(filename):
	if os.access(filename, os.F_OK):
		f = open(filename, 'r')
		if DBG: print "Reading to", filename
		r = f.readlines()
		f.close()
		return r
	else: return None

def get_results(firstname="", lastname="", source="", offline=False):
	"""Requires no more than 1 request per second"""
	if not firstname and not lastname:
		return "ERROR: Specify last name and optionally first name"

	jailbase_url = "http://www.jailbase.com/api/1/search/"
	sources = get_jailbase_sources()

	if source=="all":
		print "Searching all", len(sources), "sources. Pausing 1 sec"
		time.sleep(1.1) 	# pause a tiny bit more than 1 sec between requests
		return "Not supported yet"
		

	payload = { 'last_name': lastname, \
				'first_name': firstname, \
				'source_id': source }
	payload = urllib.urlencode(payload)

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

	if offline:
		results = get_stored_results(RECORDS_FILENAME + "-" + fullname)
		if results:
			print "======NOTE: Getting stored results from file==========="
			return results

	print "Searching criminal records for", colorify(fullname), "from", colorify(source)
	
	jailbase_url += "?" + payload
	print "Loading", jailbase_url
	req = urllib2.Request(url=jailbase_url)
	r = urllib2.urlopen(req)
	data = r.read()
	store_results(RECORDS_FILENAME + "-" + fullname, data)
	#data = json.load(r)
	return data

def colorify(txt):
	return HIGHLIGHT_COLOR + str(txt) + HIGHLIGHT_END

def main():
	parser = argparse.ArgumentParser(description='Get Criminal Records')
	parser.add_argument('--firstname', '-first', nargs='?', const=1, help="First Name of Person" )
	parser.add_argument('--lastname', '-last', nargs='?', const=1, help="Last Name of Person" )
	parser.add_argument('--source', '-source', nargs="?", help="Search all 167 sources (max of 1 request per second)" )
	parser.add_argument('--viewsources', '-viewsources', action="store_true", help="View data sources for criminal checks")
	parser.add_argument('--offline', '-offline', action="store_false", help="Retrieve offline results if available")
	args = parser.parse_args()

	if args.viewsources:
		print "The following are valid data sources for criminal checks\n"
		print ', '.join(get_jailbase_sources())[:-2]  # remove last comma
		return
	if not args.source:
		args.source = 'nj-ecdc' # default source
	if not args.firstname and not args.lastname:
		args.firstname = "John"
		args.lastname = "Smith"
	
	print ""

	if args.firstname and args.lastname:
		print get_results(firstname=args.firstname, lastname=args.lastname, source=args.source, offline=args.offline)
	elif args.firstname:
		print get_results(firstname=args.firstname, source=args.source, offline=args.offline)
	elif args.lastname:
		print get_results(lastname=args.lastname, source=args.source, offline=args.offline)


if __name__=="__main__":
	main()
