import os
from datetime import datetime
from webapp.models import Profile, FieldValue, Field
from django.conf import settings
from subprocess import call
from django.core.management.base import CommandError, NoArgsCommand
from django.db import models
from django.db import transaction
from django.utils.timezone import utc
from dateutil.relativedelta import relativedelta
import csv
import json
from subprocess import call
import criminal_scrape

class Command(NoArgsCommand):
	#@transaction.commit_manually
    help = 'load in data from csv'
    def handle_noargs(self, **options):
        # load in each of the rows of csv data and populate the database.
		query = 'Donaldson'
		results = criminal_scrape.get_results(firstname='', lastname=query, offline=False)
		#print results
		print type(results)
		
		results = json.loads(results)

		#keys = ['status', 'next_page', 'current_page', 'records', 'total_records', 'msg'	# for reference

		results = results['records']

		return

		last_name = Field.objects.get(name='last_name')
		first_name = Field.objects.get(name='first_name')
		sex_offense = Field.objects.get(name='sex_offense')
		mugshot_url = Field.objects.get(name='mugshot_url')

		i = 0
		DBG = True
		DBG = False

		for result in results:
			profile = Profile()
			profile.expiry_date = datetime.utcnow().replace(tzinfo=utc) + relativedelta(years=+1)	
			#profile.creation_date = datetime.utcnow()
			profile.save()

			fullname = str(result['name'])
			first_name = fullname.split()[0]
			last_name = fullname.split()[-1]
			sex_offenses = result['charges']
			sex_offense = str(result['charges'][0])
			mugshot = str(result['mugshot'])
			print '\n'.join([first_name, last_name, sex_offense, mugshot])
			print ""
			#break


		for line in reader:
			print "Processing data", line
			profile = Profile()
			profile.expiry_date = datetime.utcnow().replace(tzinfo=utc) + relativedelta(years=+1)	
			#profile.creation_date = datetime.utcnow()
			profile.save()
			
			# dataformat = ['Name','Address','City', 'St', 'Zip', 'County', 'Offense', 'Count', 'Compliant'] 	# for reference

			fv = FieldValue()
			fv.field = last_name
			fv.value = line[0].split(',')[1] 
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"
			
			fv = FieldValue()
			fv.field = first_name
			fv.value = line[0].split(',')[0].rstrip(', ')
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"
			
			fv = FieldValue()
			fv.field = address
			address_value = ''
			for i in range(1, 6):
				address_value += line[i] + " "
			fv.value = address_value
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"

			fv = FieldValue()
			fv.field = sex_offense
			fv.value = line[6]
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"

			fv = FieldValue()
			fv.field = sex_offense_count
			fv.value = line[7]
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"
			
			fv = FieldValue()
			fv.field = sex_offender_complaint
			fv.value = line[8].strip(', ')
			fv.profile = profile
			fv.save()
			if DBG: print "Saving " + str(fv.field), " = '" + fv.value + "'"
			
			profile.save()
			#transaction.commit

