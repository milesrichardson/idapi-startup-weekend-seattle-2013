#!../bin/python

import argparse
import csv
import string

datafile = '../msor.csv'
dataformat = ['Name','Address','City', 'St', 'Zip', 'County', 'Offense', 'Count', 'Compliant']

def get_info(firstname=None, lastname=None, selector='all'):
	fp = open(datafile, 'rb')
	reader = csv.reader(fp)	

	if firstname: firstname = firstname.upper()
	if lastname: lastname = lastname.upper() 

	if firstname is None and lastname is None:
		firstname = "John"
		lastname = "Smith"
		print "Searching for", lastname + ", " + firstname
	if firstname is None: 
		firstname = ""
		print "Searching for last name", lastname
	if lastname is None:
		print "Searching for first name ", firstname

	firstname = ", " + firstname
	lastname = lastname + ", "

	for row in reader:
		lastfirst = str(row[0])

		if firstname is ", " and lastname in lastfirst:
			print lastname.strip(', '), "found\n" + print_row(row, selector)
		elif lastname is ", " and firstname in lastfirst:
			print firstname.strip(', '), "found\n" + print_row(row, selector)
		elif lastname in lastfirst and firstname in lastfirst:
			print lastname.strip(', '), firstname.strip(', '), "found\n" + print_row(row, selector)

	fp.close()

def print_row(row, selector='all'):
	tempstr = ''
	if selector == 'all':
		start = 0
		end = len(dataformat)
	elif selector == 'address':
		start = 1
		end = 6
	elif selector == 'offense':
		start = 6
		end = 7

	for i in range(start, end):
		data = row[i].strip()
		if data == '':
			data = 'No data available'
		tempstr += dataformat[i].ljust(10) + ': ' + data + '\n'
	return tempstr

def main():
	parser = argparse.ArgumentParser(description='Get Missouri Sex Offender Report')
	parser.add_argument('--firstname', '-first', nargs='?', const=1, help="First Name of Person" )
	parser.add_argument('--lastname', '-last', nargs='?', const=1, help="Last Name of Person" )
	parser.add_argument('--selector', '-selector', nargs='?', const=1, default='all', help="Type of data: all, address, or offense" )
	args = parser.parse_args()

	if args.firstname and args.lastname:
		get_info(firstname=args.firstname, lastname=args.lastname, selector=args.selector)
	elif args.firstname:
		get_info(firstname=args.firstname, selector=args.selector)
	elif args.lastname:
		get_info(lastname=args.lastname, selector=args.selector)
	else:
		get_info()
		

if __name__=="__main__":
	main()
